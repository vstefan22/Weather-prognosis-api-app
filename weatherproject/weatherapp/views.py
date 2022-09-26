from django.shortcuts import render
import requests
import datetime

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
    temp_min = round(res['main']['temp_min'])
    temp_max = round(res['main']['temp_max'])
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    wind = res['wind']['speed']
    lon = res['coord']['lon']
    lat = res['coord']['lat']
    temp_r = res['main']['temp']
    temp = round(temp_r)
    fahrenheit = round(temp_r * 1.8000 + 32)
    min_fahrenheit = round(temp_min  * 1.8000 + 32)
    max_fahrenheit = round(temp_max  * 1.8000 + 32)
    date = datetime.date.today()
    NEW_API = 'a12da7eee42ce06e541bba202f9959ff'
    URL1 = 'http://api.openweathermap.org/data/2.5/forecast?id=524901'
    PARAMS = {'q': city, 'appid':APPID, 'units': 'metric'}
    R = requests.get(url = URL1, params = PARAMS)
    pest = R.json()
    print(pest)
    new_date_list = []
    current_temp_list = []
    pressure_list = []
    humidity_list = []
    weather_info_list = []
    weather_desc_list = []
    weather_icon_list = []
    print(current_temp_list)
    for i in range(40):
        if i % 8 == 0:
            new_date = pest['list'][i]['dt_txt']
            current_temp = round(pest['list'][i]['main']['temp'])
            date_append = datetime.datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S").date()
            pressure_new = pest['list'][i]['main']['pressure']
            humidity_new = pest['list'][i]['main']['humidity']
            weather_info = pest['list'][i]['weather'][0]['main']
            weather_desc = pest['list'][i]['weather'][0]['description']
            weather_icon = pest['list'][i]['weather'][0]['icon']
            weather_info_list.append(weather_info)
            weather_desc_list.append(weather_desc)
            weather_icon_list.append(weather_icon)
            new_date_list.append(date_append)
            pressure_list.append(pressure_new)
            humidity_list.append(humidity_new)
            current_temp_list.append(current_temp)

        else:
            pass

    context = {'description':description, 'icon':icon, 'temp':temp, 'city':city, 'fahrenheit':fahrenheit,
     'temp_min':temp_min, 'temp_max':temp_max, 'pressure':pressure, 'humidity':humidity, 'wind':wind, 'lon':lon, 
     'lat':lat, 'min_fahrenheit':min_fahrenheit,'max_fahrenheit':max_fahrenheit,
      'date':date, 'new_date_list': new_date_list, 'current_temp_list': current_temp_list, 'pressure_list':pressure_list, 'humidity_list':humidity_list, 
      'weather_info_list':weather_info_list, 'weather_desc_list':weather_desc_list, 'weather_icon_list':weather_icon_list}
    return render(request, 'weatherapp/index.html', context)
