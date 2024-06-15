#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', strict_slashes)
