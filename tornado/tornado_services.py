import tornado.ioloop
import tornado.web

from uuid_service import UUIDHandler, UUIDListHandler
from calculator_service import CalculatorHandler
from calendar_service import TodayHandler, YearInfoHandler, MonthInfoHandler
from weather_service import WeatherHandler, ForecastHandler
from text_service import TextStatsHandler, HashHandler, ReverseHandler
from number_service import RandomHandler, PrimeHandler, FactorialHandler

def make_app():
    return tornado.web.Application([
        # UUID Service routes
        (r"/api/uuid", UUIDHandler),
        (r"/api/uuid/list", UUIDListHandler),
        
        # Calculator Service routes
        (r"/api/calc/(add|subtract|multiply|divide)", CalculatorHandler),
        
        # Calendar Service routes
        (r"/api/calendar/today", TodayHandler),
        (r"/api/calendar/year", YearInfoHandler),
        (r"/api/calendar/month", MonthInfoHandler),
        
        # Weather Service routes
        (r"/api/weather", WeatherHandler),
        (r"/api/weather/forecast", ForecastHandler),
        
        # Text Service routes
        (r"/api/text/stats", TextStatsHandler),
        (r"/api/text/hash", HashHandler),
        (r"/api/text/reverse", ReverseHandler),
        
        # Number Service routes
        (r"/api/numbers/random", RandomHandler),
        (r"/api/numbers/prime", PrimeHandler),
        (r"/api/numbers/factorial", FactorialHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("API running on http://localhost:8000")
    print("\nEndpoints:")
    print("  GET /api/uuid")
    print("  GET /api/uuid/list?count=5")
    print("  GET /api/calc/add?a=5&b=3")
    print("  GET /api/calendar/today")
    print("  GET /api/weather?city=Porto Alegre")
    print("  POST /api/text/stats (JSON: {\"text\": \"hello\"})")
    print("  GET /api/numbers/random?min=1&max=10&count=3")
    print("  GET /api/numbers/prime?number=17")
    tornado.ioloop.IOLoop.current().start()