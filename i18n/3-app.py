#!/usr/bin/env python3
"""Flask app demonstrating parametrized templates with Flask-Babel"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)

class Config:
    """Configuration class for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@app.route("/")
def index():
    """Render home page with parametrized messages"""
    return render_template("3-index.html")
