#!/usr/bin/env python3
""" SessionAuth views """

from api.v1.views import app_views
from flask import abort, request, jsonify


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def safe_login() -> str:
    """ Authenticates a user and assigns a session id to the user_id """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({"error": "email missing"})
