README for Application 2: Real-Time Weather Monitoring System

Project Overview:
This project implements a real-time data processing system that retrieves weather data from the OpenWeatherMap API and provides summarized insights such as daily temperature averages, thresholds for alerts, and weather roll-ups.

Features:
Real-Time Data Retrieval: Fetches weather data for multiple Indian cities.
Temperature Conversion: Converts temperature data from Kelvin to Celsius.
Daily Weather Summaries: Calculates average, max, and min temperatures and dominant weather conditions for each day.
Alert System: Configurable threshold alerts for specific temperature conditions.
Project Structure
weather_monitor.py: Main script to fetch and process weather data.
README.md: Instructions and setup guide for running the application.

Prerequisites:
Python 3.8+
OpenWeatherMap API Key: Sign up here
pip (Python package manager)

Installation and Setup
1.Clone the Repository:
git clone https://github.com/yourusername/weather-monitoring.git
cd weather-monitoring

2.Create a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies: Install the required Python libraries:

pip install -r requirements.txt


4.Configure API Key:

Obtain an API key from OpenWeatherMap.

Update the API_KEY variable in weather_monitor.py:
API_KEY = 'your_openweathermap_api_key'


Installation and Setup
Clone the Repository:


git clone https://github.com/sarveshgaonkar/zeotap-intern-assignment.git
cd weather-monitoring
Create a Virtual Environment (optional but recommended):


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies: Install the required Python libraries:

pip install -r requirements.txt
(Ensure requirements.txt includes requests, pandas, and any other dependencies used.)

Configure API Key:

Obtain an API key from OpenWeatherMap.
Update the API_KEY variable in weather_monitor.py:

API_KEY = 'your_openweathermap_api_key'


How to Run the Application

Run the Weather Monitoring Script:

python weather_monitor.py

The application will retrieve weather data for multiple cities and display daily summaries, including average, max, and min temperatures. Alerts will trigger if any city exceeds the temperature threshold.


#Usage Example#
The script continuously retrieves weather data every 5 minutes 

Sample Output:

--- Daily Summary for Delhi ---
Average Temperature: 25.50°C
Max Temperature: 28.00°C
Min Temperature: 23.00°C
Dominant Condition: Clear

--- Daily Summary for Mumbai ---
Average Temperature: 27.80°C
Max Temperature: 29.00°C
Min Temperature: 26.50°C
Dominant Condition: Rain


Alert Example:
⚠️ Alert: Delhi's temperature exceeded 35°C for two consecutive updates!
