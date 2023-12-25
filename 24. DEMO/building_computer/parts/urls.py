from django.urls import path
from . import views

urlpatterns = [
    path('mblist/', views.MotherboardListView.as_view(), name='mb_lsit'),
    path('mbcreate/', views.MotherboardCreateView.as_view(), name='mb_create'),
    path('mbupdate/<int:pk>/', views.MotherboardUpdateView.as_view(), name='mb_update'),
    path('mbdelete/<int:pk>/', views.MotherboardDeleteView.as_view(), name='mb_delete')
]