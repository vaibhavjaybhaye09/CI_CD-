from rest_framework import serializers
from .models import WeatherRecord

# class TodoSerializer(serializers.ModelSrializer):
#     class Meta:
#         model = Todo
#         fields ='__all__'
class WeatherRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherRecord
        fields = '__all__'
        read_only_fields = ['id', 'fatched_at']

