"""
Optimize the code from the previous job with weather.
Create a WeatherForecast class, which will be used to read and write the file, as well as query the API.
The WeatherForecast class object additionally needs to correctly implement four methods:
 __setitem__
 __getitem__
 __iter__
 items

Use the following queries in your code:
weather_forecast[date] will give the weather response for the given date
weather_forecast.items() will return a tuple generator in the format (date, weather) for the already stored results when called
weather_forecast is an iterator that returns all dates for which weather is known
"""

from utils import get_date, check_rain, change_city_to_latitude_and_longitude
from file_handler import WeatherForecast

date = get_date()

city = input("Enter the city name: ")

latitude, longitude = change_city_to_latitude_and_longitude(city)

if latitude is None or longitude is None:
    print("Failed to get latitude and longitude for the city.")
    exit()

file_handler = WeatherForecast('weather_data.json')
weather_data = file_handler.load_data_from_file()

if city not in weather_data:
    weather_data[city] = {}

for entry in weather_data[city]:
    if date in entry:
        print(f"Weather for {date} in {city}: {entry[date]}")
        exit()

result = check_rain(date, latitude, longitude)
weather_data[city][date] = result
file_handler.save_data(weather_data)
print(f"Weather for {date} in {city}: {result}")
