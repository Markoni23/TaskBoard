from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('task/<int:pk>', TaskDetailView.as_view()),
    path('hi/', hi),
]