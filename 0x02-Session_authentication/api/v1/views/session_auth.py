#!/usr/bin/env python3
""" SessionAuth views """

from api.v1.views import app_views
from flask import abort, request, jsonify, make_response
from models.user import User
import os


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
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    verified_user = None
    for user in users:
        if user.is_valid_password(password):
            verified_user = user
    if not verified_user:  
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(verified_user.id)
    sess_name = os.getenv('SESSION_NAME')
    return make_response()
