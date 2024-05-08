from django.urls import path
from . import views

urlpatterns =[
    
    path('', views.Landing_1, name='Landing_1'),
    path('Register_2/', views.Register_2, name='Register_2'),
    path('Login_3/', views.Login_3, name='Login_3'),
    path('Home_4', views.Home_4, name='Home_4'),
    path('Teamates_5/', views.Teamates_5, name='Teamates_5'),
    path('Domain_Result_6/', views.Domain_Result_6, name='Domain_Result_6'),
    path('Problem_Statement_7/', views.Problem_Statement_7, name='Problem_Statement_7'),
    path('Deploy_8/', views.Deploy_8, name='Deploy_8'),
    path('Out_Database_9/', views.Out_Database_9, name='Out_Database_9'),
    path('Logout/', views.Logout, name='Logout'),
]