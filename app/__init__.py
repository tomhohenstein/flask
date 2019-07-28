# app/__init__.py

from flask import Flask

# Initialize app
app = Flask(__name__, instance_relative_config=True)

# load views
from app import views

# load config
app.config.from_object('config') 
