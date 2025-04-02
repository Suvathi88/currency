from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
            }
        else:
            weather_data = {"error": "City not found!"}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
