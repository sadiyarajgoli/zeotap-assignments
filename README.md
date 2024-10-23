# zeotap-assignments

# Rule Engine Application

## Overview
This is a simple rule engine application built using Python Flask, which utilizes MongoDB to store rules and evaluate user eligibility based on attributes like age, department, salary, and experience. The system uses an Abstract Syntax Tree (AST) to represent conditional rules.

## Features
- **Create Rules**: Define rules using a simple string format.
- **Evaluate Rules**: Check if user data meets the defined rules.
- **Store Rules**: Persist rules in a MongoDB database for retrieval and evaluation.

## Technologies Used
- Python
- Flask (for creating the API)
- PyMongo (to interact with MongoDB)
- MongoDB (for data storage)

## Getting Started

### Prerequisites
- Python 3.x
- MongoDB installed and running
- A MongoDB client (like MongoDB Compass) for database management (optional)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that MongoDB is running on your machine.

### Running the Application

1. Start the Flask application:
   ```bash
   python app.py
   ```
   The application will run on `http://127.0.0.1:5000/`.

### API Endpoints

- **Create a Rule**
  - **Endpoint**: `/create_rule`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
      "rule_string": "age > 30 AND department = 'Sales'"
    }
    ```
  - **Response**:
    ```json
    {
      "message": "Rule created successfully!"
    }
    ```

- **Evaluate a Rule**
  - **Endpoint**: `/evaluate_rule`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
      "rule_id": "<ID of the created rule>",
      "data": {
        "age": 35,
        "department": "Sales"
      }
    }
    ```
  - **Response**:
    ```json
    {
      "result": true
    }
    ```

## Example Rules
- Rule 1: `age > 30 AND department = 'Sales'`
- Rule 2: `age < 25 OR salary > 50000`

## Acknowledgments
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)
- [MongoDB Documentation](https://docs.mongodb.com/)


# assignment-2

# 🌦️ Real-Time Weather Monitoring System

## 📜 Overview
This project is a real-time weather data processing system that fetches weather conditions for multiple cities using the *OpenWeatherMap API*. It provides summarized insights using rollups and aggregates, and allows for alerting based on user-defined thresholds.

## 🛠️ Features
- *Real-Time Data Retrieval:* Continuously fetches weather data from the OpenWeatherMap API for specified cities.
- *Data Summaries:* Generates daily summaries including average temperature, max/min temperature, and dominant weather conditions.
- *Alerting System:* Triggers alerts based on user-defined thresholds for temperature and specific weather conditions.
- *Visualization:* Optional setup to visualize daily trends and historical weather data.

## 📦 Project Structure
- get_weather_data(city): Function to fetch weather data for a specified city.
- daily_summaries: Dictionary to store weather summaries for each city.
- *Alert System*: Customizable alert thresholds for extreme weather conditions.

## 🚀 Getting Started

### Prerequisites
- *Python 3.x* installed on your system.
- *API Key* from OpenWeatherMap. Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your free API key.

### Installation
1. Clone the repository:
   bash
   git clone https://github.com/sadiyarajgoli/assignments.git
   cd assignments

2. Install the required Python libraries:

pip install requests



🔧 Usage

1. Setup API Key: Open the code file and replace 'your_api_key_here' with your actual OpenWeatherMap API key:

API_KEY = 'your_actual_api_key'


2. Fetch Weather Data: Use the get_weather_data() function to fetch data for cities:

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
for city in cities:
    weather_data = get_weather_data(city)
    print(f"Weather in {city}: {weather_data}")


3. Daily Weather Summaries: Automatically process and store daily weather summaries for the specified cities:

daily_summaries = {}  # Dictionary to hold weather data

# Loop through each city and store their data in daily_summaries
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
print(daily_summaries)



🧪 Test Cases

Test the data retrieval and processing by fetching weather data for the cities:

Check the console output to see if the weather data is being fetched successfully.


⚙️ Functions Explained

1. get_weather_data(city): Fetches real-time weather data from the OpenWeatherMap API for a specific city.

2. Daily Summaries: Generates rollups of temperature and weather conditions for easy analysis.
