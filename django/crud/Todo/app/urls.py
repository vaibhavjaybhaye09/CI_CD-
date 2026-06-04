from .views import PuneWeatherAPIView

from django.urls import path

# router = DefaultRouter()
# router.register('api/weather/', PuneWeatherAPIView.as_view(), name= 'pune')

urlpatterns = [
    path('api/weather/', PuneWeatherAPIView.as_view(), name ='pune'),
]