from flask import Flask

app = Flask(__name__)

from . import quote_api  # noqa
from . import forum_api  # noqa
