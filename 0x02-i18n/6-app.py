#!/usr/bin/env python3
"""Use user locale"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Default configuration for the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Default root route"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Get user locale from URL parameters/user settings/request headers
    If none are available, then return the default locale"""
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        user_locale = users[user_id]["locale"]
        if user_locale in app.config['LANGUAGES']:
            return user_locale
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])

    # Locale from request header
    accept_lang = request.headers.get('Accpet-Language')
    if accept_lang:
        preferred_locale = accept_lang.split(',')[0]
        if preferred_locale in app.config['LANGUAGES']:
            return preferred_locale
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])

    # Find best matching locale from supported languages (default)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """This function returns the username of the user logging in"""
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        user = users.get(user_id)
        if user:
            username = user['name']
            return username


@app.before_request
def before_request():
    """This function sets the logged in user's username to be global
    so that it can be accessed from the template"""
    g.user = get_user()


if __name__ == '__main__':
    app.run()
