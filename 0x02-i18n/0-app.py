#!/usr/bin/env python3
"""basic app using Flask and Babel"""

from flask import Flask, render_template

basic_app = Flask(__name__)


@basic_app.route('/')
def welcome_hello_world():
    """basic app"""
    return render_template('0-index.html')


if __name__ == '__main__':
    basic_app.run(port="5000", host="0.0.0.0", debug=True)
