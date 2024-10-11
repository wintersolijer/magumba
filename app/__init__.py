from flask import Flask
from flask_cors import CORS
from .utils import DbHandler, PeopleHandler, QuestionHandler

app = Flask(__name__)
CORS(app)  # CORS aktivieren

PEOPLE_HANDLER = PeopleHandler()
QUESTION_HANDLER = QuestionHandler()

from app import routes

