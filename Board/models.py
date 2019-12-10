from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
