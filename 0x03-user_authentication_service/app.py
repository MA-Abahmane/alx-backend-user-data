#!/usr/bin/env python3

"""
Basic Flask app
"""

from flask import Flask, abort, jsonify, redirect, request

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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ set session login
    """
    email = request.form.get('email')
    pswd = request.form.get('password')

    if AUTH.valid_login(email, pswd):
        session_id = AUTH.create_session(email)

        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response

    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ set session logout
    """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        AUTH.destroy_session(user.id)
        return redirect("/")

    abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ profile existence validation
    """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        return jsonify({"email": user.email}), 200

    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
