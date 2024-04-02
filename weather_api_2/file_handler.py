import json


class WeatherForecast:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.filename) as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def __getitem__(self, date):
        results = {}
        for city, city_data in self.data.items():
            weather = city_data.get(date)
            if weather is not None:
                results[city] = weather
        return results

    def __setitem__(self, key, value):
        city, date = key
        if city in self.data:
            self.data[city][date] = value
        else:
            self.data[city] = {date: value}

    def __iter__(self):
        dates = set()
        for city_data in self.data.values():
            dates.update(city_data.keys())
        return iter(dates)

    def items(self):
        for city, city_data in self.data.items():
            for date, info in city_data.items():
                yield (city, date), info


"""
weather_forecast = WeatherForecast('weather_data.json')

print("Weather for 2024-03-22:", weather_forecast['2024-03-22'])

print("Stored weather data:")
for date, weather in weather_forecast.items():
    print(f"{date}: {weather}")

print("All dates for which weather is known:")
for date in weather_forecast:
    print(date)
"""
