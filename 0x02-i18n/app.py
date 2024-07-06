#!/usr/bin/env python3
"""
Simple flask app using babel
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime
from babel.dates import format_datetime


class Config:
    """ Config class for app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ / page """
    if not g.user:
        username = None
    else:
        username = g.user.get("name")
        
    tz = pytz.timezone(g.timezone)
    tz_time = datetime.now(tz)
    formatted_time = format_datetime(tz_time, locale=g.locale)
    
    try:
        int(formatted_time[0])
        formatted_time = formatted_time.replace(',', ' \u00E1')
    except Exception:
        pass

    return render_template("index.html", username=username, current_time=formatted_time)


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page."""
    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale
    elif g.user["locale"] and g.user["locale"] in app.config['LANGUAGES']:
        return g.user.get("locale")

    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    return app.Config['BABEL_DEFAULT_LOCALE']


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


def get_user():
    """returns a user dictionary or None"""
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """stores the user globally before every request"""
    g.user = get_user()
    g.timezone = get_timezone()
    g.locale = get_locale()


@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    default_tz = app.config['BABEL_DEFAULT_TIMEZONE']

    if timezone:
        try:
            tz = pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            return default_tz

    if g.user['timezone']:
        try:
            tz = pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            return default_tz

    return default_tz


if __name__ == '__main__':
    app.run(debug=True)
