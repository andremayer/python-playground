from bottle import Bottle
from datetime import datetime, date

app = Bottle()

@app.route('/date/today')
def today():
    return {'date': str(date.today()), 'day': date.today().strftime('%A')}

@app.route('/date/year')
def current_year():
    return {'year': datetime.now().year}

@app.route('/date/time')
def current_time():
    now = datetime.now()
    return {'datetime': now.isoformat(), 'timestamp': int(now.timestamp())}

@app.route('/date/weekday')
def weekday():
    return {'weekday': datetime.now().strftime('%A'), 'weekday_number': datetime.now().weekday()}