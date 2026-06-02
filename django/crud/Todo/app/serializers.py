from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSrializer):
    class Meta:
        model = Todo
        fields ='__all__'
