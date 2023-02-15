from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import ClientPermission, ContractPermission, EventPermission
from .serializers import ContractSerializer, EventSerializer, ClientSerializer
from .models import Client, Contract, Event

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [ClientPermission]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['lastname', 'email']
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
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['lastname', 'email']

    def get_queryset(self):
        return Contract.objects.all()
    
    def perform_create(self, serializer):
        client = Client.objects.get(pk=self.kwargs['client_id'])
        serializer.save(saleContact=self.request.user, client=client)
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes =  [EventPermission]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['lastname', 'email']
    def get_queryset(self):
        return Event.objects.all()
    
    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        serializer.save(client=client)