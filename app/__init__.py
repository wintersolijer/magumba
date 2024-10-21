from flask import Flask
from .utils import DbHandler, PeopleHandler, QuestionHandler, CourseHandler
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

PEOPLE_HANDLER = PeopleHandler()
QUESTION_HANDLER = QuestionHandler()
COURSE_HANDLER = CourseHandler()

from app import routes