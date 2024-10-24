README for Application 1: Rule Engine with AST

Project Overview
This project implements a Rule Engine that uses an Abstract Syntax Tree (AST) to represent, combine, and evaluate rules based on user data. The application allows for dynamic creation, combination, and evaluation of rules through a backend-only implementation.

Features
AST Creation: Parses rule strings into an AST structure.
Rule Combination: Combines multiple rules into a single AST.
Rule Evaluation: Evaluates rules against provided user data.
Test Cases: Unit tests to validate the rule engine's correctness

Project Structure
app.py: The main application file where rules are created, combined, and evaluated.
rule_engine.py: Contains the core logic for AST creation, rule combination, and rule evaluation.
tests.py: Test cases to verify the functionality of the rule engine.

Prerequisites
Python 3.8+
pip (Python package manager)

Installation and Setup
Clone the Repository:
git clone https://github.com/sarveshgaonkar/rule-engine-ast.git

cd rule-engine-ast
Create a Virtual Environment (optional but recommended):
python -m venv venv
On Windows: venv\Scripts\activate

Install Dependencies (if any):
pip install -r requirements.txt
(Note: Add a requirements.txt file if you use any external libraries. If none, this step can be skipped.)

How to Run the Application
Running the Rule Engine:
python app.py
The application will evaluate rules defined in app.py based on the sample user data and return whether the user is eligible or not.

Running Test Cases: To run the test cases and verify that the rule engine works as expected:
python tests.py

Usage Example
Example Rule:

Rule: "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"

Example User Data:

user_data = {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
}

Expected Output:

Is the user eligible? True


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
git clone https://github.com/sarveshgaonkar/weather-monitoring.git

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
On Windows: venv\Scripts\activate
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
