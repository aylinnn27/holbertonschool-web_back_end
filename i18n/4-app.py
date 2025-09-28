#!/usr/bin/env python3
"""
Basic Flask app with Babel configuration and locale selector.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Application configuration class."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best language for the user."""
    # 1. Check for locale from URL parameters
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    
    # 2. Fallback to locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Renders the 4-index.html template."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
