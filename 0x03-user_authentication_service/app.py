#!/usr/bin/env python3
""" Basic Flask app """

from auth import Auth
from flask import Flask, jsonify, request


app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def home() -> str:
    """ Returns the home JSON page """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    Return the users endpoint response
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email and pwd:
        try:
            user = AUTH.register_user(email, pwd)
            return jsonify({"email": user.email, "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def new_session() -> str:
    """
    create a new session for the user, store it the session ID as a cookie with key "session_id" on the response and return a JSON payload of the form
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
