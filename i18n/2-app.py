#!/usr/bin/env python3
"""
Flask app with Babel locale selection.
Determines the best language match based on request headers.
"""

from flask import Flask, render_template, request
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

babel = Babel()


def get_locale() -> str:
    """
    Selects the best-matching language from the request.
    Returns 'en' or 'fr' depending on the client's Accept-Language header.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Initialize Babel with the custom locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Route for the home page.
    Renders the 2-index.html template.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
