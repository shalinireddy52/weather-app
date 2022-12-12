import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # Get your API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city}: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
