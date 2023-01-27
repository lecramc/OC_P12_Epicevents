from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, ContractSerializer, EventSerializer, ClientSerializer
from .models import User, Client, Contract, Event
# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        return Client.objects.all()
class ContractView(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    
    def get_queryset(self):
        return Contract.objects.all()

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        return Event.objects.all()
