from bottle import Bottle, request
import hashlib

app = Bottle()

@app.route('/text/reverse/<text>')
def reverse_text(text):
    return {'original': text, 'reversed': text[::-1]}

@app.route('/text/upper/<text>')
def upper_text(text):
    return {'original': text, 'upper': text.upper()}

@app.route('/text/hash/<text>')
def hash_text(text):
    return {
        'text': text,
        'md5': hashlib.md5(text.encode()).hexdigest(),
        'sha256': hashlib.sha256(text.encode()).hexdigest()
    }

@app.route('/text/length/<text>')
def text_length(text):
    return {'text': text, 'length': len(text), 'words': len(text.split())}