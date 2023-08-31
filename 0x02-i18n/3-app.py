#!/usr/bin/env python3
"""Parametrize template"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Class that creates default configuration for the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """The root route"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Func that gets the default locale of the client"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
