from datetime import date
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from .models import Client, Event, Contract, Employee

class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        employee = get_object_or_404(Employee, user=request.user)
        if employee.user.is_staff:
            return True
        elif employee.type.title == "sales":
            if view.action in ['list']:
                return request.user.groups.filter(name='sales').exists()
            elif view.action in ['update']:
                client = get_object_or_404(Client, pk=view.kwargs['pk'])
                return request.user.pk == client.sales_contact.pk
            else:
                return False
        elif employee.type.title == "support":
            if view.action in ['list']:
                return request.user.groups.filter(name='support').exists()
            else:
                return False
            
            
class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        employee = get_object_or_404(Employee, user=request.user)
        if employee.user.is_staff:
            return True
        elif employee.type.title == "sales":
            if view.action in ['create', 'list']:
                return request.user.groups.filter(name='sales').exists()
            elif view.action in ['update']:
                contract = get_object_or_404(Contract, pk=view.kwargs['pk'])
                if not contract.status:
                    return request.user.pk == contract.sales_contact.pk
            else:
                return False    
        elif employee.type.title == "support":
            if view.action in ['list']:
                return request.user.groups.filter(name='support').exists()
            else :
                return False
 
class EventPermission(BasePermission):
    def has_permission(self, request, view):
        employee = get_object_or_404(Employee, user=request.user)
        if employee.user.is_staff:
            return True
        elif employee.type.title == "sales":
            if view.action in ['create', 'list']:
                return request.user.groups.filter(name='sales').exists()
            else:
                return False
        elif employee.type.title == "support":
            if view.action in ['list']:
                return request.user.groups.filter(name='support').exists()
            elif view.action in ['update']:
                event = get_object_or_404(Event, pk=view.kwargs['pk'])
                if event.event_date.date() > date.today():
                    return request.user.pk == event.support_contact.pk
            else:
                return False