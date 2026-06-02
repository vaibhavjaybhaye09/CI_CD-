from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoVIewset(viewset.Modelviewset):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    required_fields = ['todo']
    template_name = 'app/home.html'