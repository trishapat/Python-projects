import json
import requests
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim


def get_date():
    date_input = input("Enter the date in YYYY-mm-dd format or press Enter for next day:\n ")
    if not date_input:
        return (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    return date_input


def change_city_to_latitude_and_longitude(city):
    geolocator = Nominatim(user_agent="weather_forecast_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        print("Location not found.")
        return None, None


def check_rain(date, latitude, longitude):
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
           f"&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={date}&end_date={date}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(json.dumps(data))
        hourly_data = data.get('hourly', {})
        if hourly_data:
            hourly_rain = hourly_data.get('rain', [])
            if any(rain > 0 for rain in hourly_rain):
                return "It will rain"
        daily_data = data.get('daily', {})
        if daily_data:
            daily_rain_sum = daily_data.get('rain_sum', [0])[0]
            if daily_rain_sum > 0:
                return "It will rain"
    return "It will not rain"


