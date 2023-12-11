from django.urls import path
from . import views

urlpatterns = [
    path('', views.SelectAnimalView.as_view(), name='SelectAllAnimals'),
    path('<int:pk>', views.SelectAnimalView.as_view(), name='SelectOneAnimal'),
    path('add/', views.AddAnimalView.as_view(), name='AddAnimalView'),
    path('delete/<int:pk>', views.DeleteAnimalView.as_view(), name='DeleteAnimalView'),
    ]