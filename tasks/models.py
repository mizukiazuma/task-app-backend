from statistics import mode
from tkinter import CASCADE

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Task(models.Model):
    STATUS = {
        "todo": "todo",
        "doing": "doing",
        "done": "done",
    }
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=STATUS)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
