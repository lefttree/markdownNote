#!notes/bin/python
"""app module setup """
import os

from flask import Flask
from micawber import bootstrap_basic
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir

# APP_ROOT = os.path.dirname(os.path.realpath(__file__))
# DEBUG = False

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

oembed = bootstrap_basic()  # URL to video player service

from app import views, models
