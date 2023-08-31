#!/usr/bin/env python3
"""Force locale with URL parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Default config for the app instance"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Func that defines the default route"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Func that gets the locale from the args in the url and sets it
    to that or return the best match based on the default locale set
    in the Config class"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Find the best matching locale from the supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
