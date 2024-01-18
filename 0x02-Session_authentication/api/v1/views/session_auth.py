#!/usr/bin/env python3

""" Module of Index views
"""

import os
from models.user import User
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session():
    """ POST /auth_session/login
    Return:
      -  handle all routes for the Session authentication
    """
    email = request.form.get('email')
    pswd = request.form.get('password')

    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not pswd or pswd == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users or users.length <= 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(pswd):
            from api.v1.app import auth
            sess_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            sess_name = os.getenv('SESSION_NAME')
            response.set_cookie(sess_name, sess_id)
            return response

    return jsonify({ "error": "wrong password" }), 401
