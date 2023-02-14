from django.db import models
from django.contrib.auth.models import User

class ClientType(models.Model):
    title = models.CharField(max_length=30)
    
class EventStatus(models.Model):
    type = models.CharField(max_length=30)
    
class ContactType(models.Model):
    title = models.CharField(max_length=30)
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.ForeignKey(to=ContactType, on_delete=models.CASCADE)

class Client(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.ForeignKey(to=ClientType, on_delete=models.CASCADE)

class Contract(models.Model):
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

