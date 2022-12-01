# Generated by Django 4.1.3 on 2022-11-30 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bulkSaveApp', '0012_startlist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='startlist',
            options={'ordering': ['-edited_at', '-created_at']},
        ),
        migrations.RenameField(
            model_name='startlist',
            old_name='FirstName',
            new_name='Password',
        ),
        migrations.RemoveField(
            model_name='startlist',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='startlist',
            name='Phone_Number',
        ),
        migrations.RemoveField(
            model_name='startlist',
            name='email',
        ),
        migrations.AddField(
            model_name='startlist',
            name='Description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='startlist',
            name='Username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SignupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(max_length=200)),
                ('referal', models.CharField(blank=True, max_length=2000, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('repassword', models.CharField(max_length=200)),
                ('profileimage', models.ImageField(blank=True, default='images/user.png', null=True, upload_to='profilemages')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-edited_at', '-created_at'],
            },
        ),
    ]