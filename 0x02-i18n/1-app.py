#!/usr/bin/env python3

from flask import Flask, render_template
from flask_bable import Babel


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """This function defines the index/root route for the app"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
