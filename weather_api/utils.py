
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
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&date={date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rainfall = data.get('rainfall', 0)
        if rainfall > 0:
            return "It will rain"
        elif rainfall == 0:
            return "It will not rain"
    return "I don't know"
