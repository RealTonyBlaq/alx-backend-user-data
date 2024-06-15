#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, jsonify, request
from auth import Auth


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
    if request.method == "POST":
        email = request.form.get('email')
        pwd = request.form.get('password')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
