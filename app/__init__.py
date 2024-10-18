from flask import Flask
from .utils import DbHandler, PeopleHandler, QuestionHandler, CourseHandler


app = Flask(__name__)

PEOPLE_HANDLER = PeopleHandler()
QUESTION_HANDLER = QuestionHandler()
COURSE_HANDLER = CourseHandler()

from app import routes