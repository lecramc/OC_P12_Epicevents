from rest_framework import serializers
from .models import User, Client, Contract, Event

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = "__all__"

class ContractSerializer(serializers.Serializer):
    class Meta:
        model = Contract
        fields = "__all__"

class EventSerializer(serializers.Serializer):
    class Meta:
        model = Event
        fields = "__all__"
