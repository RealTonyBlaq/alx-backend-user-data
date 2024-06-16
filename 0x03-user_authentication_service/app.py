#!/usr/bin/env python3
""" Basic Flask app """

from auth import Auth
from flask import (abort, Flask, jsonify, make_response,
                   redirect, request, url_for)


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


@app.route('/sessions', methods=['POST', 'DELETE'],
           strict_slashes=False)
def new_session() -> str:
    """
    POST /sessions
    create a new session for the user, store it the session ID
    as a cookie with key "session_id" on the response and
    return a JSON payload of the form

    DELETE /sessions
    If the user exists destroy the session and redirect to GET /.
    If the user does not exist, respond with a 403 HTTP status.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = make_response(
                jsonify({"email": email, "message": "logged in"}), 200)
            response.set_cookie('session_id', session_id)
            return response
        abort(401)
    elif request.method == 'DELETE':
        cookie = request.cookies.get('session_id')
        if cookie:
            user = AUTH.get_user_from_session_id(cookie)
            if user:
                AUTH.destroy_session(user.id)
                return redirect(url_for('home'))
        abort(403)


@app.route('/profile', strict_slashes=False)
def profile() -> str:
    """ Returns a JSON payload of the user if it exists """
    cookie = request.cookies.get('session_id')
    if cookie:
        user = AUTH.get_user_from_session_id(cookie)
        if user
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
