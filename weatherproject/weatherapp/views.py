from django.shortcuts import render
import  requests

def index(request):

    if request.method == 'POST':
        city = request.POST['city']

    else: 
        city = 'Amsterdam'
    APPID = '7f79df561afd9b1f86cac2c3bdb2665e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': APPID, 'units':'metric'}
    r = requests.get(url = URL, params = PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp_min = res['main']['temp_min']
    temp_max = res['main']['temp_max']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    wind = res['wind']['speed']
    lon = res['coord']['lon']
    lat = res['coord']['lat']
    temp_r = res['main']['temp']
    temp = round(temp_r)
    fahrenheit = round(temp_r * 1.8000 + 32)
    context = {'description':description, 'icon':icon, 'temp':temp, 'city':city, 'fahrenheit':fahrenheit,
     'temp_min':temp_min, 'temp_max':temp_max, 'pressure':pressure, 'humidity':humidity, 'wind':wind, 'lon':lon, 'lat':lat}
    return render(request, 'weatherapp/index.html', context)
