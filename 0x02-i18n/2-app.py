#!/usr/bin/env python3
"""
Simple flask app using babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config class for app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ / page """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
    print(app.config['LANGUAGES'])
