from datetime import date
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from .models import Client, Event, Contract, Employee

class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        user = get_object_or_404(Employee, user=request.user)
        if user.type.title == "manager":
            if view.action in ['list', 'retrieve', 'create', 'update', 'destroy']:
                return request.user.groups.filter(name='manager').exists()
            else:
                return False
        elif user.type.title == "sales":
            if view.action in ['list', 'retrieve', 'create']:
                return request.user.groups.filter(name='sales').exists()
            elif view.action in ['update']:
                client = get_object_or_404(Client, pk=view.kwargs['pk'])
                return request.user.is_sales_contact(client)
            else:
                return False
        elif user.type.title == "support":
            if view.action in ['list', 'retrieve']:
                return request.user.groups.filter(name='support').exists()
            else:
                return False
            
    def has_object_permission(self, request, view, obj):
        user = get_object_or_404(Employee, user=request.user)
        if user.type.title == "support" and obj in Client.objects.filter(
            events__support_contact=request.user
        ):
            return request.user.groups.filter(name='support').exists()
            
class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        user = get_object_or_404(Employee, user=request.user)
        if user.type.title == "manager":
            if view.action in ['create', 'list', 'retrieve', 'update', 'destroy']:
                return request.user.groups.filter(name='manager').exists()
            else:
                return False

        elif user.type.title == "sales":
            if view.action in ['create', 'list', 'retrieve']:
                return request.user.groups.filter(name='sales').exists()
            elif view.action in ['update']:
                contract = get_object_or_404(Contract, pk=view.kwargs['pk'])
                if not contract.status:
                    return request.user.is_sales_contact(contract)
            else:
                return False    
       
 
class EventPermission(BasePermission):
    def has_permission(self, request, view):
        user = get_object_or_404(Employee, user=request.user)
        if user.type.title == "manager":
            if view.action in ['create', 'list', 'retrieve', 'update', 'destroy']:
                return request.user.groups.filter(name='manager').exists()
            else:
                return False
        elif user.type.title == "sales":
            if view.action in ['create', 'list', 'retrieve']:
                return request.user.groups.filter(name='sales').exists()
            else:
                return False
        elif user.type.title == "support":
            if view.action in ['list', 'retrieve']:
                return request.user.groups.filter(name='support').exists()
            elif view.action in ['update']:
                event = get_object_or_404(Event, pk=view.kwargs['pk'])
                if event.event_date.date() > date.today():
                    return request.user.is_support_contact(event)
            else:
                return False