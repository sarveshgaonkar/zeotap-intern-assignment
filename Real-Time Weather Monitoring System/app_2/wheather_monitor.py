import requests
import pandas as pd
import time
from datetime import datetime

# Global Variables
API_KEY = '06adae213cebd900bc76fdf12c3f513a'  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
weather_records = []  # To store weather data

# Function to fetch data from OpenWeatherMap API
def get_weather_data(city):
    try:
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(base_url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return response.json()  # Returns the weather data in JSON format
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Could not fetch data for {city}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to process and return a formatted weather record
def process_weather_data(city):
    data = get_weather_data(city)
    if data:
        return {
            'city': city,
            'temp_celsius': round(kelvin_to_celsius(data['main']['temp']), 2),
            'feels_like': round(kelvin_to_celsius(data['main']['feels_like']), 2),
            'weather_condition': data['weather'][0]['main'],
            'timestamp': datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }
    return None

# Function to store the weather data in memory
def store_weather_data():
    global weather_records
    for city in CITIES:
        record = process_weather_data(city)
        if record:
            weather_records.append(record)
            print(f"Weather data for {city} stored.")
        else:
            print(f"Failed to fetch or store weather data for {city}.")

# Function to aggregate weather data and print daily summaries
def aggregate_weather_data():
    if not weather_records:
        print("No weather data available to aggregate.")
        return
    
    df = pd.DataFrame(weather_records)
    grouped = df.groupby('city')

    for city, data in grouped:
        avg_temp = data['temp_celsius'].mean()
        max_temp = data['temp_celsius'].max()
        min_temp = data['temp_celsius'].min()
        dominant_condition = data['weather_condition'].mode()[0]

        print(f"\n--- Daily Summary for {city} ---")
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Max Temperature: {max_temp:.2f}°C")
        print(f"Min Temperature: {min_temp:.2f}°C")
        print(f"Dominant Condition: {dominant_condition}")
        print(f"Records collected at: {data['timestamp'].values[-1]}")
    print("\n--------------------------------")

# Function to check alert thresholds for each city
def check_alerts(threshold_temp=35):
    for city in CITIES:
        city_data = [record for record in weather_records if record['city'] == city]
        
        if len(city_data) >= 2:
            if city_data[-1]['temp_celsius'] > threshold_temp and city_data[-2]['temp_celsius'] > threshold_temp:
                print(f"⚠️ Alert: {city}'s temperature exceeded {threshold_temp}°C for two consecutive updates!")

# Function to continuously monitor weather
def monitor_weather(interval=300):
    while True:
        print("\nFetching new weather data...\n")
        store_weather_data()
        aggregate_weather_data()
        check_alerts()
        print("\nWaiting for the next update...\n")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_weather()  # Starts the weather monitoring system
