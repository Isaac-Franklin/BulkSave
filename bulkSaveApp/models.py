from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class SignupModel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200)
    referal = models.CharField(max_length=2000, blank=True, null=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    repassword = models.CharField(max_length=200)
    # profileimage = models.ImageField(
    #     upload_to='profilemages', blank=True, null=True, default="images/user.png")
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
    
    def __str__(self):
        return self.fullname
    
    
    
class LoginForm(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    

class AllContacts(models.Model):
    FullName = models.CharField(max_length=200)
    Signature = models.CharField(max_length=200)
    Phone_Number  = models.CharField(max_length=200, blank=True, null=True)
    Phone_Number2  = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.FullName
    
    
    
class StartList(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Signature = models.CharField(max_length=200)
    Title = models.CharField(max_length=2000, blank=True, null=True)
    Description = models.CharField(max_length=5000, blank=True, null=True)
    Access = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
    
    def __str__(self):
        return self.Signature