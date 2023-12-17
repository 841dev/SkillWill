from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main_Page, name='Main_Page'),
    path('list/', views.List_Users, name='List_Users'),
    path('create/', views.Create_User, name='Create_User'),
    path('update/<int:user_id>/', views.Update_User, name='Update_User'),
    path('delete/', views.Delete_User, name='Delete_User')

    ]