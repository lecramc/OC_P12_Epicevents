# Generated by Django 4.1.6 on 2023-02-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_alter_client_sales_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='payment_due',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(),
        ),
    ]
