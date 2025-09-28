#!/usr/bin/env python3
"""Flask app demonstrating locale selection using URL, user preference, and headers"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
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
    """Determine the locale with priority: URL parameter > user > header > default"""
    # 1. URL parameter
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    # 2. User preference
    if getattr(g, "user", None):
        user_locale = g.user.get("locale")
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    # 3. Request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def index():
    """Render home page with optional user welcome"""
    return render_template("6-index.html")
