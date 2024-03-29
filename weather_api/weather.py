"""
Write a program to check if it will rain on a given day. The application should work as follows:

The program asks for which date to check the weather. The date must be in the format YYYY-mm-dd, e.g. 2022-11-03.
If no date is given, the application will take the next day as the date searched for.
The application will make a query to the API to look for the weather condition.

There are three possible information for rainfall:
It will rain (for a result greater than 0.0)
Will not rain (for a result equal to 0.0)
Don't know (when the result is not there for some reason or the value is negative)

Query results should be saved to a file. If the date you are looking for is already in the file,
do not make a query to the API, but return the result from the file.

In the URL, fill in the parameters: latitude, longitude and searched_date
"""
# weather.py
from utils import get_date, check_rain, change_city_to_latitude_and_longitude
from file_handler import FileHandler

date = get_date()

city = input("Enter the city name: ")

latitude, longitude = change_city_to_latitude_and_longitude(city)

if latitude is None or longitude is None:
    print("Failed to get latitude and longitude for the city.")
    exit()

file_handler = FileHandler('weather_data.json')
weather_data = file_handler.load_data_from_file()

if city not in weather_data:
    weather_data[city] = []

for entry in weather_data[city]:
    if date in entry:
        print(f"Weather for {date} in {city}: {entry[date]}")
        exit()

result = check_rain(date, latitude, longitude)
entry = {date: result}
weather_data[city].append(entry)
file_handler.save_data(weather_data)
print(f"Weather for {date} in {city}: {result}")
