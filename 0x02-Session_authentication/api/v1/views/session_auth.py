#!/usr/bin/env python3

""" Module of Index views
"""

import os
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session():
    """ POST /auth_session/login
    Return:
      -  handle all routes for the Session authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or len(users) <= 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            sess_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            sess_name = os.getenv('SESSION_NAME')
            response.set_cookie(sess_name, sess_id)
            return response

    return jsonify({"error": "wrong password"}), 401


@app_views.route('auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    """ DELETE /api/v1/auth_session/logout
    Return:
      -  deletes the user session / logout
    """
    from api.v1.app import auth
    response = auth.destroy_session(request)
    if response:
        return jsonify({}), 200
    abort(404)
