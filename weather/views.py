from django.shortcuts import render, redirect
from django.conf import settings as se
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        if city:
            url = se.WEATHER_URL.format(city=city, api=se.WEATHER_API_KEY)
            weather = requests.get(url).json()
            city_weather = {
                'city':city,
                'temperature':weather['main']['temp'],
                'description':weather['weather'][0]['description'],
                'icon':weather['weather'][0]['icon'],
            }
            context = {
                "city_weather":city_weather
            }
            return render(request, 'weather/index.html', context)
        else:
            return render(request, 'weather/index.html')
    else:
        return redirect('/')