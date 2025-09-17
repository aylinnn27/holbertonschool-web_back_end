#!/usr/bin/env python3
"""Module of Index views for API v1"""

from flask import jsonify, abort
from api.v1.views import app_views  # use the imported blueprint

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """GET /api/v1/status
    Return:
        - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """GET /api/v1/stats
    Return:
        - the number of each object
    """
    from models.user import User
    stats = {"users": User.count()}
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_route() -> str:
    """GET /api/v1/unauthorized
    Trigger 401 Unauthorized error
    """
    abort(401)
