from django.contrib import admin
from .models import Client, Employee, Event, Contract, ClientType, ContactType, EventStatus
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'
class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "email", "mobile", "company")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "date_created", "event_status")

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "sales_contact", "client", "date_created", "status", "amount")

@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    
@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    
@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "type")


