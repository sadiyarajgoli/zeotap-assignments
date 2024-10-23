import requests
import time

API_KEY = 'b94ed28d7f897fd4f71802e4a827a5c9'  # Replace with your actual OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None


cities = ['Pune','Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
for city in cities:
    weather_data = get_weather_data(city)
    print(f"Weather in {city}: {weather_data}")
    time.sleep(1)  

    
daily_summaries = {}

for city in cities:
    weather_data = get_weather_data(city)  
    if weather_data:  
        main_weather = weather_data['weather'][0]['main']  
        current_temp = weather_data['main']['temp']  
        feels_like_temp = weather_data['main']['feels_like']  
        timestamp = weather_data['dt']  
        
        
        daily_summaries[city] = {
            'main_weather': main_weather,
            'current_temp': current_temp,
            'feels_like_temp': feels_like_temp,
            'timestamp': timestamp
        }

        
{
    'Delhi': {
        'main_weather': 'Clear',
        'current_temp': 30,
        'feels_like_temp': 32,
        'timestamp': 1634085600
    },
    'Mumbai': {
        'main_weather': 'Rain',
        'current_temp': 28,
        'feels_like_temp': 29,
        'timestamp': 1634085600
    },
    # ... more cities
}
print(daily_summaries)