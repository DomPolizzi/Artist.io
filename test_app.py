import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import APP
from models import setup_db, Artist, Video


class ArtistIoTest(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.testing = True
        self.client = self.app.test_client

        # Test database name
        self.database_name = "capstonetest"
        self.database_path = "postgresql://postgres:viktor@localhost:5432/" + self.database_name
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables
            self.db.create_all()

        self.new_artist = {
            'name': 'Charlie Brown',
            'age': '25',
            'style': 'musician'
        }
        self.new_video = {
            'title' : 'Jazz Theory',
            'type' : 'Stream'
        }

        def tearDown(self):
            """Executed after each test"""
            pass

    # TESTS START HERE

    def test_homepage(self):
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

    def test_get_artist(self):
        res = self.client().get('/artists')
        data = json.loads(res.data)

        artists = Artist.query.order_by(Artist.id).all()        
        output = [artist.format() for artist in artists]
       
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], output)

    def test_get_artist(self):
        res = self.client().get('/videos')
        data = json.loads(res.data)

        videos = Video.query.order_by(Video.id).all()        
        output = [video.format() for video in videos]
       
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['videos'], output)


    def test_get_artist_by_id(self):
        res = self.client().get('/artists/1')
        data = json.loads(res.data)

        artist = Artist.query.get(self)        
        output = artist.format()
       
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], output)

if __name__ == "__main__":
    unittest.main()
