from bottle import Bottle, request

app = Bottle()

@app.route('/calc/add/<a:float>/<b:float>')
def add(a, b):
    return {'operation': 'add', 'a': a, 'b': b, 'result': a + b}

@app.route('/calc/subtract/<a:float>/<b:float>')
def subtract(a, b):
    return {'operation': 'subtract', 'a': a, 'b': b, 'result': a - b}

@app.route('/calc/multiply/<a:float>/<b:float>')
def multiply(a, b):
    return {'operation': 'multiply', 'a': a, 'b': b, 'result': a * b}

@app.route('/calc/divide/<a:float>/<b:float>')
def divide(a, b):
    if b == 0:
        return {'error': 'Division by zero'}
    return {'operation': 'divide', 'a': a, 'b': b, 'result': a / b}