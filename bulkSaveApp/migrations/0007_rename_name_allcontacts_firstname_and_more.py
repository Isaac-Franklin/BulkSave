# Generated by Django 4.1.3 on 2022-11-29 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulkSaveApp', '0006_testmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allcontacts',
            old_name='Name',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='allcontacts',
            old_name='Additional_Name',
            new_name='LastName',
        ),
        migrations.RenameField(
            model_name='allcontacts',
            old_name='Phone_1_Value',
            new_name='Phone_Numer',
        ),
        migrations.RemoveField(
            model_name='allcontacts',
            name='Given_Name',
        ),
    ]