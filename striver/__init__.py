from flask import Flask

app = Flask(__name__)

from striver import api  # imports the api from api.py
