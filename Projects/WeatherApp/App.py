from flask import Flask, render_template, request
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

api_key = os.getenv('WEATHER_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_info = None
    error = None
    
    if request.method == 'POST':
        city = request.form['city']
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
        )
        forecast_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&APPID={api_key}"
        )
        if weather_data.json()['cod'] == '404':
            error = "City not found"
        else:
            data = weather_data.json()
            forecast = forecast_data.json()
            daily_forecast = []
            for i in range(0, 40, 8):
                day = forecast['list'][i]
                daily_forecast.append({
                    'date': datetime.fromtimestamp(day['dt']).strftime('%A, %b %d'),
                    'temp': round(day['main']['temp']),
                    'weather': day['weather'][0]['main'],
                })
            weather_info = {
            'city': city,
            'weather': data['weather'][0]['main'],
            'temperature': round(data['main']['temp']),
            'humidity': data['main']['humidity'],
            # use timezone offset from API
            'sunrise': datetime.utcfromtimestamp(
                data['sys']['sunrise'] + data['timezone']
            ).strftime('%I:%M %p'),
            'sunset': datetime.utcfromtimestamp(
                data['sys']['sunset'] + data['timezone']
            ).strftime('%I:%M %p'),
            'forecast': daily_forecast
        }
            
    return render_template('index.html', weather=weather_info, error=error)

if __name__ == '__main__':
    app.run(debug=True)