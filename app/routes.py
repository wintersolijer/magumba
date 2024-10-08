from app import app, PEOPLE_HANDLER, QUESTION_HANDLER
from flask import render_template, request


@app.route('/')
def home():
    return render_template('index.html')

@app.post('/create_person')
def create_person():
    payload = request.json

    first_name: str = payload['first_name']
    last_name: str = payload['last_name']
    email: str = payload['email']
    password: str = payload['password']
    birthday = payload['birthday']

    return PEOPLE_HANDLER.create_person(first_name, last_name, email, password, birthday)

@app.post('/login')
def login():
    payload = request.json

    email: str = payload['email']
    password: str = payload['password']

    return PEOPLE_HANDLER.check_login(email, password)

@app.get('/get_ranking')
def get_ranking():
    return PEOPLE_HANDLER.get_ranking()

@app.post('/add_question')
def addQuestion():
    """
    payload:
    {
        "question": {
            "type": "string"
        },
        "answers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string"
                    },
                    "isTrue":{
                        "type": "boolean"
                    }
                }
            }
        },
        "points": {
            "type": "integer"
        }
    }
    """
    payload = request.json
    question: str = payload['question']
    answers: str = payload['answers']
    points: int = payload['points']

    return QUESTION_HANDLER.add_question(question, answers, points)