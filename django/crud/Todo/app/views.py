import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import WeatherRecordSerializer

class PuneWeatherAPIView(APIView):
    def get(self, request, fromat = None):
        LATITUDE = 18.5204
        LONGITUDE = 73.8567
        url = f"httpsL://open-meto.com{LATITUDE}&longitude={LONGITUDE}&current=emprature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m"

        try :
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            current = response.json().get("current", {})

            # 1 map raw data api data to match you serializer/model fields

            api_data ={
                "city":"Pune",
                "temprature":current.get("temprature_2m"),
                "feels_like":current.get("apparent_temprature"),
                "humidity":current.get("relative_humidity_2m"),
                "wind_speed":current.get("wind_speed_10m"),
            }

            #2. pass data to serializers fro validation

            serializer =WeatherRecordSerializer(data=api_data)
            if serializer.is_valid():
                #3. save data automatically into databaseto table
                serializer.save()
                return response(serializer.data, status= status.HTTP_201_CREATED)


            return Response(serializer.error, status = status.HTTP_400_BAD_REQUIEST)
        
        except requests.exceptions.RequestException as e:            return Response(
                {"error": "Failed to fetch external weather data"},
                status =  status.HTTP_503_SERVICE_UNAVAILABLE
            )



