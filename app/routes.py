from app import app, PEOPLE_HANDLER, QUESTION_HANDLER
from flask import render_template, request


@app.route('/')
def home():
    return render_template('index.html')

@app.post('/create_person')
def create_person():
    """
    payload: 
    {
        "first_name": {
            "type": "string"
        },
        "last_name": {
            "type": "string"
        },
        "email": {
            "type": "string",
        },
        "password": {
            "type": "string"
        },
        "birthday": {
            "type": "string",
            "format": "date"
        }
    }
    """

    payload = request.json

    first_name: str = payload['first_name']
    last_name: str = payload['last_name']
    email: str = payload['email']
    password: str = payload['password']
    birthday = payload['birthday']

    return PEOPLE_HANDLER.create_person(first_name, last_name, email, password, birthday)

@app.post('/login')
def login():
    """
    payload: 
    {
        "email": {
            "type": "string",
        },
        "password": {
            "type": "string"
        }
    }
    """

    payload = request.json

    email: str = payload['email']
    password: str = payload['password']

    return PEOPLE_HANDLER.check_login(email, password)

@app.post('/add_points')
def add_points():
    """
    payload: 
    {
        "user_id": {
            "type": "string"
        },
        "points": {
            "type": "integer"
        }
    }
    """

    payload = request.json
    id: str = payload['user_id']
    points: int = payload['points']

    return PEOPLE_HANDLER.add_points(id, points)

@app.post('/get_points')
def get_points():
    """
    payload:
    {
        "user_id": {
            "type": "string"
        }
    }
    """

    payload = request.json
    id: str = payload['user_id']

    return PEOPLE_HANDLER.get_points(id)


@app.get('/get_ranking')
def get_ranking():
    return PEOPLE_HANDLER.get_ranking()

@app.post('/add_question')
def add_question():
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

@app.get('/get_rand_question')
def get_rand_question():
    return QUESTION_HANDLER.get_random_question()

@app.post('/create_material')
def create_material():
    payload = request.json

    material_name: str = payload['material_name']
    course_name: str = payload['course_name']
    pdf_name: str = payload['pdf_name']

    return PEOPLE_HANDLER.add_course_material(material_name, course_name, pdf_name)