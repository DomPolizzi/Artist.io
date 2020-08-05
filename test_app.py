import os
import unittest
import json
from sqlalchemy import DateTime
from datetime import datetime
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

        self.artist = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVKNHZEUnhBakREWDhTZkxrei15VCJ9.eyJpc3MiOiJodHRwczovL2Rldi01NmQzY3RuNy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxY2I1OTlkYThmZmEwMDNkMWY4NWQ1IiwiYXVkIjoiY2FwcGVyIiwiaWF0IjoxNTk2NTIwNjU5LCJleHAiOjE1OTY2MDcwNTksImF6cCI6IlJCQ3JuNlZTRzUzYmN4bmdadlhEYnZOWUR3YmNHbVhRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDphcnRpc3QiLCJwYXRjaDp2aWRlbyIsInBvc3Q6dmlkZW8iXX0.skac2WqBAg1noVRzvhhp3EA_8LS0_o_HTYXkxGGahNgRM4a8Bggws2cQGw5Ch-iDzW0q0bXT2CWw4yy7ylYm7-9rwqZYBfdKzPhwNV8tCGpb7IrAwyeQMPJehAJSPhPwOoeEPtwIGldz-f0AW0CPbX-Y4-LYUGwD2s4-KcXg9PZ2IpSB3QzV0iAiHQV5Lg0mtPXJQ0s7fDxVAaSZ1_3B2VzHV_qVZYpzOnHoWjIkS_fQuamvxoybDBj_H9S-pt0DeeFDzK46VKCCRZfLci2ImDvCEbNnR53DiCDg1W4Og_IJ0Hnc0B3tBFPNvrQULqD3h6mLFG88YI-Ikedbzl7dUw'
        self.mod = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVKNHZEUnhBakREWDhTZkxrei15VCJ9.eyJpc3MiOiJodHRwczovL2Rldi01NmQzY3RuNy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxYzlmMzBkYThmZmEwMDNkMWY3NjQ1IiwiYXVkIjoiY2FwcGVyIiwiaWF0IjoxNTk2NjA2OTYzLCJleHAiOjE1OTY2OTMzNjMsImF6cCI6IlJCQ3JuNlZTRzUzYmN4bmdadlhEYnZOWUR3YmNHbVhRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0IiwiZGVsZXRlOnZpZGVvIiwicGF0Y2g6YXJ0aXN0IiwicGF0Y2g6dmlkZW8iLCJwb3N0OnZpZGVvIl19.fqcqWAIJUP1cA3h8taN_-bX3ESh5iwCvQE_5ck24tZy4uLwbNQzB3W--awNl1cbGFmPPRXDhYvzVTG-KVKbvUuyMMlr549nLrUVRT0z0GnHO5vwpcos10pRHaCFKxx_KlY_BZ6WLPNl9IXCPrY8wzByEJ_xnYak2yM-rXhskW6SDiBkCE3C8QzMfc6Zwbh2pbF5jWwIIn9v-xL_kmsmSQQYY1OB6GZuKpMbb9fn6rTojU34vcPYVkakzpeGFMvLVjaYW0TSef08rbSNL4mlu9SaOWopn2EljPhhOsz8Mtki0snyWjBbbY3bZlZSmcPNVrM7LjlErIZPbAtQNuk0cQQ'
        self.badfuckingtoken = 'bullshit'

        self.new_artist = {
            'name': 'Charlie Brown',
            'age': '25',
            'style': 'musician'
        }
        self.new_video = {
            'title': 'Jazz Theory',
            'type': 'Stream'
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    # TESTS START HERE

    def test_homepage(self):
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

    def test_post_artist(self):
        res = self.client().post('/artists', json=self.new_artist)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], {'name': 'Charlie Brown', 'id': 1, 'age': '25',
                                          'style': 'musician'})

    def test_get_artist(self):
        res = self.client().get('/artists')
        data = json.loads(res.data)

        artists = Artist.query.order_by(Artist.id).all()
        output = [artist.format() for artist in artists]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], output)

    def test_get_video(self):
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

        artist = Artist.query.get(self).first().id
        output = artist.format()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], output)

    def test_post_video_w_token(self):
        res = self.client().post('/add-videos',
                                 headers={"Authorization": "Bearer {}".format(self.mod)}, json=self.new_video)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['videos'], {'title': 'Jazz Theory', 'id': 3,
                                          'type': 'Stream'})

if __name__ == "__main__":
    unittest.main()
