#!/usr/bin/env python3
"""Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """A Class that defines the configuration for the flask Instance"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """This function defines the index/root route for the app"""
    return render_template('2-index.html')


@bable.localeselector
def get_locale():
    """A function that determines the best lang for a client"""
    # Get user's preferred language from the request
    user_lang = request.accept_languages.values()
    # Find the best_matching locale from the supported languages
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    return best_match


if __name__ == '__main__':
    app.run()
