from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoVIewset(viewset.Modelviewset):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    renderer_classes = [renderers.JSONRenderer]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    required_fields = ['todo']
    template_name = 'app/home.html'