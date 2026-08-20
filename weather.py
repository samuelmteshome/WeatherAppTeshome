import requests
import os
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("Key loaded:", API_KEY is not None)
print("Key length:", len(API_KEY) if API_KEY else 0)

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)

    # 4. Parse JSON
    data = response.json()

    if response.status_code == 404:
        print(f'Could not find "{city}". Check the spelling and try again')
    if response.status_code != 200:
        print("OpenWeather request failed.")
        return
    print("Status code:", response.status_code)
    print("Response:", data)

    # 5. Parse JSON
    data = response.json()
    
    # 6. Extract key info
    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    
    # 7. Print
    print(f"\nWeather for {city_name}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.title()}")
    return True
while True:
    city = input("Enter a U.S. city: ").strip()

    if not city:
        print("Please enter a city name.")
        continue

    if get_weather(city):
        break

# Try it
get_weather("Raleigh")

def main():
    # ask user for city
    # call get_weather()
    city = input("Enter a U.S. city: ")
    get_weather(city)

if __name__ == "__main__":
    main()