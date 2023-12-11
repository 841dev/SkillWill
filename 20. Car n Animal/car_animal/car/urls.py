from django.urls import path
from . import views

urlpatterns = [
    path('', views.SelectCarView.as_view(), name='SelectAllCars'),
    path('<int:pk>', views.SelectCarView.as_view(), name='SelectOneCar'),
    path('add/', views.AddCarView.as_view(), name='AddCarlView'),
    path('delete/<int:pk>', views.DeleteCarView.as_view(), name='DeleteCarView'),
    ]