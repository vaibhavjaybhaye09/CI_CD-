from django.db import models
# Create your models here.

class Todo(models.Model):
    id = models.AutoField(unique=True)
    todo = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)