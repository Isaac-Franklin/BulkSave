# Generated by Django 4.1.3 on 2022-11-30 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulkSaveApp', '0013_loginform_alter_startlist_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupmodel',
            name='profileimage',
        ),
    ]