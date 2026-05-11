from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
api_key='a6b39327394feebeb4743b3ac2506a83'

@app.route('/', methods=['GET','POST'])
def home():
    weather_info=None
    error=None
    if request.method=='POST':
        city = request.form['city']
user_input=input("Enter the city you are in:")

weather_data=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)
if weather_data.json()['cod']=='404':
    error="City not found"
else:
    data=weather_data.json()

    weather=data['weather'][0]['main']
    temperature=round(data['main']['temp'])
    humidity=data['main']['humidity']
    sunrise=datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')
    sunset=datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')

    print(f"Weather: {weather}, Temperature: {temperature}°F")
    print(f"Humidity: {humidity}%")
    print(f"Sunrise: {sunrise}, Sunset: {sunset}")