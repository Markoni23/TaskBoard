from django.shortcuts import render
from .models import *

# Create your views here.

def tasks(request):
    return render(request, 'tasks.html', {'tasks':Task.objects.all()})