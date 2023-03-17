# Generated by Django 4.1.6 on 2023-02-24 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_client_date_created_alter_client_date_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]