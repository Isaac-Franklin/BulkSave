from django.urls import path
from . import views


urlpatterns = [
    # path('', views.LandingPage, name='LandingPage'),
    path('exportdata/<str:Signature>/', views.export_to_csv, name='export_to_csv'),
    path('', views.LandingPage, name='LandingPage'),
    path('general/', views.General, name='General'),
    path('collectdata/<str:Signature>/', views.CollectData, name='CollectData'),
    path('startlist/', views.StartListPage, name='StartListPage'),
    path('allavailablelists/', views.AllAvailableLists, name='AllAvailableLists'),
    path('signuppage/', views.SignupPage, name='SignupPage'),
    path('loginpage/', views.Loginpage, name='Loginpage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('deletelist/<str:Signature>/', views.DeleteList, name='DeleteList'),
    path('listdetails/<str:Signature>/', views.ListDetailsPage, name='ListDetailsPage'),
    path('exportList/<str:Signature>/', views.export_to_csv, name='export_to_csv'),
    
]
