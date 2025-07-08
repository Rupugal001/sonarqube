from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "f75885cd16f3f2ef1cd70d9e250de34d"

INDIAN_CITIES = ["Trichy", "Covai", "Madurai"]

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city in INDIAN_CITIES:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&units=metric&appid={API_KEY}"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                  weather_data = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"]
                }
            else:
                error = "City not found! Please try again."
    
    return render_template("index.html", weather=weather_data, error=error, cities=INDIAN_CITIES)

if __name__ == "__main__":
    app.run(debug=True)
