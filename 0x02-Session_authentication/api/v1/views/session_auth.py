#!/usr/bin/env python3
""" SessionAuth views """

from api.v1.views import app_views
from flask import abort, request, jsonify
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def safe_login() -> str:
    """ Authenticates a user and assigns a session id to the user_id """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
        for user in users:
            if 
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404