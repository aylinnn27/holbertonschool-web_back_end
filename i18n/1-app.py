#!/usr/bin/env python3
"""
Flask app with basic Babel setup.
This app configures available languages and default locale/timezone.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask-Babel.
    Defines available languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Route for the home page.
    Renders the 1-index.html template.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
