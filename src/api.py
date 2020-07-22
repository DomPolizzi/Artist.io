import os
from flask import (
    Flask,
    request,
    jsonify,
    abort,
    request,
    Response
)
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import setup_db, Artist, Video, db_drop_and_create_all
from auth.auth import AuthError, requires_auth, get_token_auth_header

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#


def create_app(test_config=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

   # db_drop_and_create_all()

    # ===================
    # ROUTES
    # ===================

    @app.route('/')
    def get_greeting():
        return "Salutations Comrade. No front end created yet. see README.md"

    @app.route('/artists')
    def get_artists():

        artists = Artist.query.all()

        if len(artists) == 0:
            print("No Artists Found")
            abort(401)

        return jsonify({
            'success': True,
            'artists': "Test works, someone is found"
        })

    @app.route('/add-artists', methods=['POST'])
    def create_artist():

        body = request.get_json()

        artist_name = body.get('name')
        artist_age = body.get('age')
        artist_style = body.get('style')

        try:
            new_artist = Artist(
                name=artist_name, age=artist_age, style=artist_style)
            print('Post initialized')
            new_artist.insert()

        except Exception as e:
            print(e)
            print("something went wrong")
            print(e.args)
            abort(400)

        return jsonify({
            "success": True,
            "artists": new_artist.format
        }), 200

    @app.route('/videos')
    def get_videos():
        videos = Video.query.all()

        if len(videos) == 0:
            print("test works, no videos found")
            abort(401)

        return jsonify({
            'success': True,
            'artists': "Test works, one video is found"
        })

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
