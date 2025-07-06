import tornado.web
import random
import datetime

class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        city = self.get_argument("city", "Unknown City")
        
        conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Foggy", "Windy"]
        temperature = random.randint(-10, 35)
        humidity = random.randint(30, 90)
        condition = random.choice(conditions)
        
        self.set_header("Content-Type", "application/json")
        self.write({
            "city": city,
            "temperature_celsius": temperature,
            "condition": condition,
            "humidity_percent": humidity,
            "timestamp": datetime.datetime.now().isoformat()
        })

class ForecastHandler(tornado.web.RequestHandler):
    def get(self):
        city = self.get_argument("city", "Unknown City")
        days = int(self.get_argument("days", 5))
        days = min(days, 7)
        
        conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Foggy", "Windy"]
        forecast = []
        
        for i in range(days):
            forecast.append({
                "day": i + 1,
                "temperature_celsius": random.randint(-10, 35),
                "condition": random.choice(conditions),
                "humidity_percent": random.randint(30, 90)
            })
        
        self.set_header("Content-Type", "application/json")
        self.write({
            "city": city,
            "forecast_days": days,
            "forecast": forecast
        })