#!/usr/bin/env python3
"""Flask app to demonstrate forcing locale with URL parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Configuration class for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@babel.locale_selector
def get_locale() -> str:
    """Determine the best match for supported languages based on URL parameter"""
    # Check URL parameter first
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Fallback to request accept languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the home page"""
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(debug=True)
