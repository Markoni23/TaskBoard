from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', tasks),
    path('hi/', hi),
]