import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import APP
from models import setup_db, Artist, Video


class ArtistIoTest(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app()
        self.client = self.app.test_client

        # Test database name
        self.database_name = "capstonetest"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', database_name)
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

        def tearDown(self):
            """Executed after each test"""
            pass

    # TESTS START HERE

    def test_homepage(self):
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

    def test_create_new_artist(self):


        res = self.client().post('/add-artists', json=self.new_artist)
        data = json.loads(res.data)

        artist = Artist.query.filter(
            Artist.id == data['created']).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(artist)

if __name__ == "__main__":
    unittest.main()
