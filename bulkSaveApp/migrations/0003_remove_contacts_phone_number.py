# Generated by Django 4.1.3 on 2022-11-29 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulkSaveApp', '0002_alter_contacts_phone_1_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='phone_number',
        ),
    ]
