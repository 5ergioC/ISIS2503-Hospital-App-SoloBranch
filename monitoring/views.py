from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def healtCheck(request):
    return HttpResponse('ok')