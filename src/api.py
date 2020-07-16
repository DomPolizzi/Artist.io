import os
from flask import (
    Flask,
    request,
    jsonify,
    abort,
    Request,
    Response
)
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import setup_db, Artist, Video, db_drop_and_create_all
from .auth.auth import AuthError, requires_auth, get_token_auth_header

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello"
        if excited == 'true':
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/artists')
    def get_artists():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/videos')
    def get_videos():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

# =================================================================
#  Error Handlers
# =================================================================

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Unathorized'
        }), 401

    @app.errorhandler(404)
    def unreachable(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Server Error'
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(auth):
        a_error = jsonify(auth.error)
        a_error.status_code = auth.status_code
        return a_error

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
