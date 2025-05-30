from django.urls import path
from . import views

urlpatterns = [
    path('mri/', views.mri_list, name='mri_list'),
    path('mri/create/', views.mri_create, name='mri_create'),
]
