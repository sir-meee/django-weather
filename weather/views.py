import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=48f737f5bee28dbe93b34fbb92f67ff2'
    city = 'Nairobi'

    r = requests.get(url.format(city)).json()
    # print(r.text)

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    # print(city_weather)

    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)