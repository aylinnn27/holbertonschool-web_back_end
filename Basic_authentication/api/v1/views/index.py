#!/usr/bin/env python3
""" Module of Index views
"""

from flask import jsonify, abort
from api.v1.views import app_views  # imported blueprint

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_route() -> str:
    """ GET /api/v1/unauthorized
    Trigger 401 Unauthorized error
    """
    abort(401)  # This triggers the 401 error handler in app.py
