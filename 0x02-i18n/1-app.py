#!/usr/bin/env python3
"""basic app using Flask and Babel"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """basic app configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


basic_app = Flask(__name__)
babel = Babel(basic_app)
basic_app.config.from_object(Config)


@basic_app.route('/')
def welcome_hello_world():
    """basic app"""
    return render_template('1-index.html')


if __name__ == '__main__':
    basic_app.run(port="5000", host="0.0.0.0", debug=True)
