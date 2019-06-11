# Generated by Django 2.2.2 on 2019-06-11 15:54

from django.db import migrations
from django.core.management import call_command

fixture = 'db'

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='users')

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]