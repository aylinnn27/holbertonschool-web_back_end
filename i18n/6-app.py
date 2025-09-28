#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Configuration class for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

def get_user():
    """Returns a user dictionary based on the 'login_as' URL parameter."""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request():
    """Sets the user as a global on flask.g before each request."""
    g.user = get_user()

    # NOTE: In a real app, this is where you'd set the user locale for the template
    # Example:
    # g.locale = get_locale() # Though get_locale is called automatically by Babel

@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages based on priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # 1. Locale from URL parameters
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Renders the index template."""
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(debug=True)
