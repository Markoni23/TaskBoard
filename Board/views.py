from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

def tasks(request):
    return render(request, 'tasks.html', {'tasks':Task.objects.all()})


class TaskListView(ListView):
    queryset = Task.objects.all()
    context_object_name = 'tasks'
    template_name = 'Board/tasks.html'
    

class TaskDetailView(DetailView):
    model = Task


def hi(request):
    return render(request, 'Board/main.html')