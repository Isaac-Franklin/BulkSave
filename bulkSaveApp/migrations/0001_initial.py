# Generated by Django 4.1.3 on 2022-11-29 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Given_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Additional_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Phone_1_Value', models.IntegerField(blank=True, max_length=255, null=True)),
                ('phone_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-edited_at', '-created_at'],
            },
        ),
    ]