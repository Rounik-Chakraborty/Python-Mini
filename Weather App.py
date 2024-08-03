import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

# Function to get weather data
def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if data.get("cod") == 200:
            main = data.get("main", {})
            weather = data.get("weather", [{}])[0]
            temp = main.get("temp")
            pressure = main.get("pressure")
            humidity = main.get("humidity")
            weather_desc = weather.get("description")
            icon = weather.get("icon")
            
            return {
                "temp": temp,
                "pressure": pressure,
                "humidity": humidity,
                "description": weather_desc,
                "icon": icon
            }
        else:
            print(f"API Error: {data.get('message')}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to update weather information in the GUI
def show_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    weather = get_weather(city)
    
    if weather:
        temp_label.config(text=f"Temperature: {weather['temp']}°C")
        pressure_label.config(text=f"Pressure: {weather['pressure']} hPa")
        humidity_label.config(text=f"Humidity: {weather['humidity']}%")
        description_label.config(text=f"Description: {weather['description']}")
        
        icon_url = f"http://openweathermap.org/img/wn/{weather['icon']}@2x.png"
        try:
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
        except Exception as e:
            print(f"Icon Error: {e}")
            icon_label.config(image=None)
    else:
        messagebox.showerror("Error", "City not found or invalid city name. Please try again.")

# Setting up the main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")

# Adding a label and entry for the city
city_label = tk.Label(app, text="Enter City:", font=("bold", 14))
city_label.pack(pady=10)
city_entry = tk.Entry(app, width=25, font=("bold", 14))
city_entry.pack(pady=5)

# Adding a button to fetch weather
get_weather_button = tk.Button(app, text="Get Weather", command=show_weather, font=("bold", 14))
get_weather_button.pack(pady=20)

# Adding labels to display weather information
temp_label = tk.Label(app, text="", font=("bold", 14))
temp_label.pack(pady=5)
pressure_label = tk.Label(app, text="", font=("bold", 14))
pressure_label.pack(pady=5)
humidity_label = tk.Label(app, text="", font=("bold", 14))
humidity_label.pack(pady=5)
description_label = tk.Label(app, text="", font=("bold", 14))
description_label.pack(pady=5)
icon_label = tk.Label(app, image=None)
icon_label.pack(pady=5)

# Running the application
app.mainloop()
