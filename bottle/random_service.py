from bottle import Bottle
import random
import string

app = Bottle()

@app.route('/random/number')
def random_number():
    return {'random_number': random.randint(1, 100)}

@app.route('/random/number/<min_val:int>/<max_val:int>')
def random_range(min_val, max_val):
    return {'min': min_val, 'max': max_val, 'random': random.randint(min_val, max_val)}

@app.route('/random/string/<length:int>')
def random_string(length):
    chars = string.ascii_letters + string.digits
    result = ''.join(random.choice(chars) for _ in range(length))
    return {'length': length, 'random_string': result}

@app.route('/random/choice')
def random_choice():
    choices = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    return {'choices': choices, 'selected': random.choice(choices)}