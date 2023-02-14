from rest_framework import viewsets, permissions
from .serializers import ContractSerializer, EventSerializer, ClientSerializer
from .models import Client, Contract, Event, Employee
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import ClientPermission, ContractPermission, EventPermission

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [ClientPermission]
    
    def get_queryset(self):
        return (
            Client.objects.filter(
                events__support_contact=self.request.user
            ).distinct()
            if self.request.user.groups.filter(name='support').exists()
            else Client.objects.all()
        )


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [ContractPermission]


    def get_queryset(self):
        return Contract.objects.all()

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes =  [EventPermission]

    def get_queryset(self):
        return Event.objects.all()
