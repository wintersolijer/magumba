from flask import Flask
from .utils import DbHandler, PeopleHander


app = Flask(__name__)

PEOPLE_HANDLER = PeopleHander()

from app import routes