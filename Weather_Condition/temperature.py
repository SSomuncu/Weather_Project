import requests
from tkinter import *

city = input("Enter City: ")
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

data = requests.get(url).json()

temp = int(data['main']['temp'] - 273.15)
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']

print("Temperature: ", temp, "°C")
print("wind :", wind)
print("Pressure: ", pressure)
print("Humidity: ", humidity)
print("Description: ", description)