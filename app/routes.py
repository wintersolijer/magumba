from app import app
from flask import render_template, request


@app.route('/')
def home():
    return render_template('index.html')

@app.post('/create_person')
def create_person():
    payload = request.json
    print(payload)
    return payload