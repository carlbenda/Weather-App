from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm

def index(request):
    # API key from weatherapi.com
    api_key = 'e70525237f7646c5af765352251402'
    forecast_url = 'http://api.weatherapi.com/v1/forecast.json'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            # Clear all existing cities before adding new one
            City.objects.all().delete()
            form.save()
            return redirect('index')
    else:
        form = CityForm()
    
    cities = City.objects.all()
    weather_data = []
    forecast_data = []
    
    for city in cities:
        params = {
            'key': api_key,
            'q': city.name,
            'days': 7,  # 7 days forecast
            'aqi': 'no'
        }
        
        try:
            response = requests.get(forecast_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Current weather data
            city_weather = {
                'city': city.name,
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'icon': data['current']['condition']['icon'],
                'humidity': data['current']['humidity'],
                'wind': data['current']['wind_kph'],
                'country': data['location']['country'],
                'region': data['location']['region'],
                'localtime': data['location']['localtime'],
            }
            
            weather_data.append(city_weather)
            
            # Forecast data for the next 7 days
            days_forecast = []
            for day in data['forecast']['forecastday']:
                forecast_day = {
                    'date': day['date'],
                    'max_temp': day['day']['maxtemp_c'],
                    'min_temp': day['day']['mintemp_c'],
                    'condition': day['day']['condition']['text'],
                    'icon': day['day']['condition']['icon'],
                    'chance_of_rain': day['day']['daily_chance_of_rain'],
                    'humidity': day['day']['avghumidity'],
                    'wind': day['day']['maxwind_kph'],
                }
                days_forecast.append(forecast_day)
            
            forecast_data.append({
                'city': city.name,
                'days': days_forecast
            })
            
        except Exception as e:
            # If the API request fails, remove the city from the database
            city.delete()
            continue
    
    context = {
        'weather_data': weather_data,
        'forecast_data': forecast_data,
        'form': form
    }
    
    return render(request, 'weather/index.html', context)
