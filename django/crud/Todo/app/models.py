from django.db import models
# Create your models here.

# class Todo(models.Model):
#     id = models.AutoField(unique=True)
#     todo = models.CharField(max_length=200, unique=True)
#     status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     class Meta:
#         ordering = ['- created_at']

class WeatherRecord(models.Model):
    city = models.CharField(max_length=100,default='Pune')
    temperature =models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temprature}°C at {self.fetched_at}"
    