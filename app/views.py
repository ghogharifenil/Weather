from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from datetime import datetime
import pytz

def weather(request):
    weather_data = None

    if request.method == "POST":
        city = request.POST.get("city")

        api_key = "youapikey"

        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

        response = requests.get(url)
        data = response.json()

        print("Status Code:", response.status_code)
        print("API Response:", data)

        # API success
        if "current" in data:
            weather_data = {
                "icon": data["current"]["condition"]["icon"],
                "city": data["location"]["name"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "humidity": data["current"]["humidity"],
                "wind": data["current"]["wind_kph"],
                "condition": data["current"]["condition"]["text"],
                "time": data["location"]["localtime"],
            }

        # API error
        else:
            weather_data = {
                "error": data.get(
                    "error", {}
                ).get(
                    "message",
                    "Something went wrong."
                )
            }
        context = {
        'india_time': datetime.now(
            pytz.timezone('Asia/Kolkata')
        ).strftime('%I:%M %p'),

        'usa_time': datetime.now(
            pytz.timezone('America/New_York')
        ).strftime('%I:%M %p'),

        'london_time': datetime.now(
            pytz.timezone('Europe/London')
        ).strftime('%I:%M %p'),

        'japan_time': datetime.now(
            pytz.timezone('Asia/Tokyo')
        ).strftime('%I:%M %p'),

        'sydney_time': datetime.now(
            pytz.timezone('Australia/Sydney')
        ).strftime('%I:%M %p'),
    }
    return render(
        request,
        "html/home.html",
        {
            "weather": weather_data , 
            'context':context
        }
    )