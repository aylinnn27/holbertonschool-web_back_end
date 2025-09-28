#!/usr/bin/env python3
"""Flask app demonstrating mock user login with Flask-Babel"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _  # noqa: F401
from typing import Optional

app = Flask(__name__)

class Config:
    """Configuration class for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Optional[dict]:
    """Return user dict from users table based on login_as URL parameter"""
    login_as = request.args.get("login_as")
    if login_as:
        try:
            user_id = int(login_as)
            return users.get(user_id)
        except ValueError:
            return None
    return None

@app.before_request
def before_request():
    """Set the current user in flask.g.user before each request"""
    g.user = get_user()

@babel.locale_selector
def get_locale():
    """Select locale: URL parameter > user preference > request header > default"""
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    if getattr(g, "user", None) and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def index():
    """Render home page with optional user welcome"""
    return render_template("5-index.html")
