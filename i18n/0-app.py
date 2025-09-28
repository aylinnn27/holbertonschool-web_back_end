#!/usr/bin/env python3
"""
Basic Flask app that serves a single route.
The app renders an HTML template with a welcome message.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Route for the home page.
    Renders the 0-index.html template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
  
