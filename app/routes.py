from app import app, PEOPLE_HANDLER
from flask import render_template, request


@app.route('/')
def home():
    return render_template('index.html')

@app.post('/create_person')
def create_person():
    payload = request.json

    first_name = payload['first_name']
    last_name = payload['last_name']
    email = payload['email']
    password = payload['password']
    birthday = payload['birthday']

    return PEOPLE_HANDLER.createPerson(first_name, last_name, email, password, birthday)