from flask import Flask
from .utils import DbHandler, PeopleHandler, QuestionHandler


app = Flask(__name__)

PEOPLE_HANDLER = PeopleHandler()
QUESTION_HANDLER = QuestionHandler()

from app import routes