from django.urls import path
from . import views

urlpatterns = [
    path('mri/command/', views.mri_command, name='mri_command'),   # writes
    path('mri/query/', views.mri_list_query, name='mri_query'),    # reads
]
