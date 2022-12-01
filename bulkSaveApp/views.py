from django.shortcuts import render, redirect
import csv
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
# Create your views here.


def SignupPage(request):
    if request.method == 'POST':
        # form = SignupForm(request.POST, request.FILES)
        fullname = request.POST['fullname']
        username = request.POST['username']
        referal = request.POST['referal']
        email = request.POST['email']
        # profilepicture = request.FILES.get('profileimage', False)
        password = request.POST['password']
        retypepassword = request.POST['repassword']
        
        if password != retypepassword:
            messages.error(request, 'Passwords Are Not Same')
            return redirect('Signup')

        data = SignupModel.objects.filter(username=username)
        if data:
            messages.error(request, 'Sorry, Username Is Already Taken')
            return redirect('SignupPage')
        else:
            messages.success(request, 'Registration Successful')
            form = SignupModel(fullname=fullname, username=username, email=email, referal=referal, password=password, repassword=retypepassword, profileimage=profilepicture)

            user = User.objects.create_user(
                first_name=fullname, email=email, password=password, username=username)
            login(request, user)
            user.save()
            form.save()
            return redirect('Loginpage')
            messages.success(request, 'Registration Successful')
        # messages.success(request, 'Registration Failed')
    return render(request, 'bulkSaveApp/Signup.html')



def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Login Failed: User Does Not Exit')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('AllAvailableLists')

        else:
            messages.error(request, 'Login Failed: Please Try Again')
            return render(request, 'bulSaveApp/Login.html')
    return render(request, 'bulkSaveApp/Login.html')



def logoutUser(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return render(request, 'bulkSaveApp/Logout.html')


def CollectData(request, Signature):
    mycontacts = StartList.objects.get(Signature = Signature)
    if request.method == 'POST':
        FullName = request.POST['fullname']
        Signature = request.POST['signature']
        Phone_Number = request.POST['phonenumber']
        Phone_Number2 = request.POST['phonenumber2']
        form = AllContacts(FullName = FullName, Signature = Signature, Phone_Number = Phone_Number, Phone_Number2 = Phone_Number2)
        form.save()
        messages.success(request, 'Details Submitted Successful')
        return redirect('AllAvailableLists')
    context = {'Signature': Signature, 'mycontacts' : mycontacts}
    return render(request, 'bulkSaveApp/contactlist.html', context)



def export_to_csv(request, Signature):                  
    mycontacts = AllContacts.objects.filter(Signature = Signature)
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename = Bulk Save Contacts Export.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Family Name', 'Phone 1 - Value', 'Phone 2 - Value'])
    contacts_fields = mycontacts.values_list('FullName', 'Signature', 'Phone_Number', 'Phone_Number2' )
    for contact in contacts_fields:
        writer.writerow(contact)
    return response



def AllAvailableLists(request):
    allLists = StartList.objects.all().order_by('-created_at')
    numoflists = allLists.count()
    if request.user.is_authenticated:
        data = StartList.objects.filter(Username=request.user.last_name).first()
    else:
        return redirect('Loginpage')
    context = {'allLists': allLists, 'numoflists':numoflists, 'data':data}
    return render(request, 'bulkSaveApp/allavailablelists.html', context)


def LandingPage(request):
    testfile = TestModel.objects.all()
    context = {'testfile': testfile}
    return render(request, 'bulkSaveApp/landingpage.html', context)


def General(request):
    return render(request, 'general.html')



def StartListPage(request):
    if request.method == 'POST':
        user = request.user
        Username = request.POST['Username']
        Signature = request.POST['signature']
        Title = request.POST['title']
        Description = request.POST['Description']
        Access = request.POST['access']
        Password = request.POST['Password']
        
        data = SignupModel.objects.get(username = Username)
        if data:
            pass
        else:
            messages.error(request, 'Sorry, Your User Was Not Found, Kindly Signup To Create A List')
            return render(request, 'bulkSaveApp/startlist.html')
        
        
        data3 = SignupModel.objects.get(password=Password)
        if data3:
            pass
        else:
            messages.error(request, 'Sorry, Password Is Incorrect')
            return render(request, 'bulkSaveApp/startlist.html')
        
        data2 = StartList.objects.filter(Signature=Signature)
        if data2:
            messages.error(request, 'Sorry, Your Signature Has To Be Unique, Kindly Enter Another One')
            return render(request, 'bulkSaveApp/startlist.html')
        else:
            form = StartList(user = user, Username = Username, Description = Description, Title = Title, Access=Access, Password = Password,  Signature = Signature)
            form.save()
            messages.success(request, 'New List Created Successfully')
            return redirect('AllAvailableLists')
    if request.user.is_authenticated:
        data = StartList.objects.filter(Username=request.user.last_name).first()
    else:
        return redirect('Loginpage')
    context = {'data':data}
    return render(request, 'bulkSaveApp/startlist.html', context)



def DeleteList(request, Signature):
    allLists = StartList.objects.filter(Signature=Signature)
    if request.method == "POST":
        allLists.delete()
        messages.success(request, 'List Successfully Deleted!')
        return redirect('AllAvailableLists')
    context = {'allLists':allLists}
    return render(request, 'bulkSaveApp/DeleteList.html', context)


def ListDetailsPage(request, Signature):
    allLists = StartList.objects.get(Signature=Signature)
    alllistContacts = AllContacts.objects.filter(Signature=Signature)
    numofcontact = alllistContacts.count()
    context = {'allLists':allLists, 'alllistContacts':alllistContacts, 'numofcontact':numofcontact}
    return render(request, 'bulkSaveApp/ListDetails.html', context)