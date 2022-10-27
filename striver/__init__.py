from flask import Flask

app = Flask(__name__)

# import api.py
from striver import quote_api  # noqa
