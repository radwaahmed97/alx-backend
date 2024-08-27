#!/usr/bin/env python3
"""basic app using Flask and Babel"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """basic app configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


basic_app = Flask(__name__)
babel = Babel(basic_app)
basic_app.config.from_object(Config)
basic_app.url_map.strict_slashes = False


@babel.localeselector
def get_locale():
    """determines the best match with our supported languages"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@basic_app.route('/')
def welcome_hello_world():
    """basic app"""
    return render_template('3-index.html')


if __name__ == '__main__':
    basic_app.run(port="5000", host="0.0.0.0", debug=True)
