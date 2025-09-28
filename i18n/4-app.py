#!/usr/bin/env python3
"""
Flask application configured for internationalization (i18n)
that supports forcing the locale via a URL parameter.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

# Configuration class
class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Initialize application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determine the best matching language for the request.
    1. Check if 'locale' parameter is present in the URL query string.
    2. If present and supported, return its value.
    3. Otherwise, fall back to the best match from accepted languages.
    """
    # 1. Check for locale in URL parameters
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param

    # 2. Fall back to best match from accepted languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Renders the 4-index.html template."""
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
