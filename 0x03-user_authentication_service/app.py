#!/usr/bin/env python3

"""
Basic Flask app
"""

from flask import Flask, jsonify, request

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """ Home page
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def set_user():
    """ Register User
    """
    try:
        email = request.form.get('email')
        pswd = request.form.get('password')

        AUTH.register_user(email, pswd)
        return jsonify({"email": f"{email}", "message": "user created"})

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
