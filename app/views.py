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
            Client.objects.filter(event__support_contact=self.request.user)
            if self.request.user.groups.filter(name="support")
            else Client.objects.all()
        )
 

class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [ContractPermission]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['client__lastname', 'client__email', "date_created", "payment_due"]

    def get_queryset(self):
        return Contract.objects.filter(
                sales_contact=self.request.user
            )
    
    def perform_create(self, serializer):
        client = Client.objects.get(pk=self.kwargs['client_id'])
        serializer.save(sales_contact=self.request.user, client=client)
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes =  [EventPermission]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['client__lastname', 'client__email', "event_date"]
    def get_queryset(self):
        return Event.objects.all()
    
    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        serializer.save(client=client)