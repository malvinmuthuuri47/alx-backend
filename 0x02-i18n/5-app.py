#!/usr/bin/env python3
"""Mock logging in"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Default config for the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFUALT_TIMEZONE = 'UTC'
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
    """root route of the function"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """Gets the default locale for the user/returns the default user
    locale specified in the config class if the user defined locale
    is unavailable"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Find best_matching locale from supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Returns a username from the users dictionary"""
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        user = users.get(user_id)
        if user:
            username = user['name']
            return username
    else:
        return None


@app.before_request
def before_request():
    """A function that makes the username accessible globally"""
    g.user = get_user()


if __name__ == '__main__':
    app.run()
