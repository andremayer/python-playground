import tornado.web
import datetime
import calendar

class TodayHandler(tornado.web.RequestHandler):
    def get(self):
        today = datetime.date.today()
        self.set_header("Content-Type", "application/json")
        self.write({
            "date": today.isoformat(),
            "day_name": today.strftime("%A"),
            "month_name": today.strftime("%B"),
            "year": today.year,
            "day_of_year": today.timetuple().tm_yday
        })

class YearInfoHandler(tornado.web.RequestHandler):
    def get(self):
        year = int(self.get_argument("year", datetime.date.today().year))
        is_leap = calendar.isleap(year)
        self.set_header("Content-Type", "application/json")
        self.write({
            "year": year,
            "is_leap_year": is_leap,
            "days_in_year": 366 if is_leap else 365
        })

class MonthInfoHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            year = int(self.get_argument("year", datetime.date.today().year))
            month = int(self.get_argument("month", datetime.date.today().month))
            
            if month < 1 or month > 12:
                self.set_status(400)
                self.write({"error": "Month must be between 1 and 12"})
                return
                
            days_in_month = calendar.monthrange(year, month)[1]
            month_name = calendar.month_name[month]
            
            self.set_header("Content-Type", "application/json")
            self.write({
                "year": year,
                "month": month,
                "month_name": month_name,
                "days_in_month": days_in_month
            })
        except ValueError:
            self.set_status(400)
            self.write({"error": "Invalid year or month format"})