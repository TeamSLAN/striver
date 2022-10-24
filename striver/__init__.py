from flask import Flask

app = Flask(__name__)

from striver import api  # nopep8
