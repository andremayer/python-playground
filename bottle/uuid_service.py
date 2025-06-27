from bottle import Bottle
import uuid

app = Bottle()

@app.route('/uuid')
def generate_uuid():
    return {'uuid': str(uuid.uuid4())}

@app.route('/hello/<name>')
def hello_name(name):
    return {'message': f'Hello, {name}!'}

@app.route('/health')
def health_check():
    return {'status': 'ok'}