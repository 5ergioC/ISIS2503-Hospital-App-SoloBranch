from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('MRI/', views.MRI_list),
    path('MRIcreate/', csrf_exempt(views.MRI_create), name='MRICreate'),
]