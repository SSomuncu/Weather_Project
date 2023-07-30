import requests
from tkinter import *
from PIL import ImageTk, Image

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "06c921750b9a82d8f5d1294e1586276f"
icon_url = "https://openweathermap.org/img/wn/{}@2x.png"

def get_weather(city):
    params = {'q': city, 'appId': api_key, 'lang':'tr'}
    data = requests.get(url, params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city, country, temp, icon, condition)
def main():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        location_label['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_label['text'] = '{} °C'.format(weather[2])
        condition_label['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(weather[3]), stream=True).raw))
        icon_label.configure(image=icon)
        icon_label.image = icon




#UI
FONT = ("Calibri", 15, "normal")

window = Tk()
window.geometry("300x600")

window.title("Weather")
window.config(padx=30, pady=30)
window.config(bg="light green")

photo = PhotoImage(file="weather.png")
photo_label = Label(image=photo)
photo_label.pack()

city_entry = Entry(window, justify='center')
#city_entry.insert(string="Enter your city...", index=0)
city_entry.pack(ipady=5, pady=10,padx=10, fill=BOTH)
city_entry.focus()

weather_button = Button(window, text="Bring The Weather", font=FONT, command=main)
weather_button.pack(fill=BOTH, ipady=10, padx=10)

icon_label = Label(window, pady=10)
icon_label.pack()

location_label = Label(window, font=FONT, pady=10)
location_label.pack()

temp_label = Label(window, font=FONT, pady=10)
temp_label.pack()

condition_label = Label(window, pady=10, font=FONT)
condition_label.pack()


window.mainloop()
