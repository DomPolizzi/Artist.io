import os
import unittest
import mock
import datetime
import json
from sqlalchemy import DateTime
from flask_sqlalchemy import SQLAlchemy

from app import APP
from models import setup_db, Artist, Video, get_date


class ArtistIoTest(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.testing = True
        self.client = self.app.test_client

        # Test database name
        self.database_name = "capstonetest"
        self.database_path = "postgresql://postgres:ravyn@localhost:5432/" + self.database_name
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables
            self.db.create_all()

        self.artist = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVKNHZEUnhBakREWDhTZkxrei15VCJ9.eyJpc3MiOiJodHRwczovL2Rldi01NmQzY3RuNy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxY2I1OTlkYThmZmEwMDNkMWY4NWQ1IiwiYXVkIjoiY2FwcGVyIiwiaWF0IjoxNTk2NTIwNjU5LCJleHAiOjE1OTY2MDcwNTksImF6cCI6IlJCQ3JuNlZTRzUzYmN4bmdadlhEYnZOWUR3YmNHbVhRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDphcnRpc3QiLCJwYXRjaDp2aWRlbyIsInBvc3Q6dmlkZW8iXX0.skac2WqBAg1noVRzvhhp3EA_8LS0_o_HTYXkxGGahNgRM4a8Bggws2cQGw5Ch-iDzW0q0bXT2CWw4yy7ylYm7-9rwqZYBfdKzPhwNV8tCGpb7IrAwyeQMPJehAJSPhPwOoeEPtwIGldz-f0AW0CPbX-Y4-LYUGwD2s4-KcXg9PZ2IpSB3QzV0iAiHQV5Lg0mtPXJQ0s7fDxVAaSZ1_3B2VzHV_qVZYpzOnHoWjIkS_fQuamvxoybDBj_H9S-pt0DeeFDzK46VKCCRZfLci2ImDvCEbNnR53DiCDg1W4Og_IJ0Hnc0B3tBFPNvrQULqD3h6mLFG88YI-Ikedbzl7dUw'
        self.mod = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVKNHZEUnhBakREWDhTZkxrei15VCJ9.eyJpc3MiOiJodHRwczovL2Rldi01NmQzY3RuNy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxYzlmMzBkYThmZmEwMDNkMWY3NjQ1IiwiYXVkIjoiY2FwcGVyIiwiaWF0IjoxNTk3MDE1NzA5LCJleHAiOjE1OTcxMDIxMDksImF6cCI6IlJCQ3JuNlZTRzUzYmN4bmdadlhEYnZOWUR3YmNHbVhRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0IiwiZGVsZXRlOnZpZGVvIiwicGF0Y2g6YXJ0aXN0IiwicGF0Y2g6dmlkZW8iLCJwb3N0OnZpZGVvIl19.TGpK4vKI3gQKF87swStVp4oF7oGlqccAF1Mh5zoRWERCJdvqHbdvHIFD_Zn4Ikp1fH25d-3UzZLADud8sKTfc8F08FdtDNsqnKMnQOx764KezmDXlhfj9jTQeZVTPFyTVMVe6pQWUAhvKMvgSPL7_-gSW3kiXlSSHbMpDfRWlPLVjafU6E7ZC6_0XL4NOvV_NmjN3XOZPzo_ksGQcEsHECCgXpTAxsd5j0_pMRIszLWoyEg-9zmglNmWID2nr7IqVeTLoPkp4ckvJiD0OSRrX1F8iOBKj6Vr6iSVOvj8JbLzlBpx2D5UOQxDGfY4kzAmps0j-2BZQDbKm68pW58ngw'
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
        print('Test Endpoint for Posting Artists: ')
        res = self.client().post('/artists', json=self.new_artist)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], {
                         'name': 'Charlie Brown', 'id': 1, 'age': 25, 'style': 'musician'})

    def test_get_artist(self):
        print('Testing to check if Artists exist: ')
        res = self.client().get('/artists')
        data = json.loads(res.data)

        artists = Artist.query.order_by(Artist.id).all()
        output = [artist.format() for artist in artists]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], output)

    def test_post_video_w_token(self):
        print('Test Endpoint for Posting Videos: ')
        res = self.client().post('/add-videos',
                                 headers={"Authorization": "Bearer {}".format(self.mod)}, json=self.new_video)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['videos'], {'title': 'Jazz Theory', 'id': 1,
                                          'type': 'Stream', 'date': data['videos']['date']})

    def test_get_video(self):
        print('Testing to check if Videos exist: ')
        res = self.client().get('/videos')
        data = json.loads(res.data)

        videos = Video.query.order_by(Video.id).all()
        output = [video.format() for video in videos]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['videos'], output)

    def test_get_artist_by_id(self):
        print('Testing to check on one artist in specific: ')
        res = self.client().get('/artists/1')
        data = json.loads(res.data)

        artist = Artist.query.get(self).first().id
        output = artist.format()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists'], output)

    def test_patch_artist_w_token(self):
        print('Testing to Patch one Video in specific with Mod Token: ')
        video = Video(name="")
        video.insert()

        res = self.client().patch('/videos/',
                                  headers={"Authorization": "Bearer {}".format(self.mod)}, json=self.new_video)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['video_id'], video.id)

    def test_patch_video_w_token(self):
        print('Testing to Patch one Artist in specific with Mod Token: ')
        video = Video(name="")
        video.insert()

        res = self.client().patch('/videos/',
                                  headers={"Authorization": "Bearer {}".format(self.mod)}, json=self.new_video)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['video_id'], video.id)

    def test_delete_artist_w_token(self):
        print('Testing to Delete one artist in specific Mod Token: ')
        artist = Artist(name="")
        artist.insert()

        res = self.client().delete('/artists/',
                                   headers={"Authorization": "Bearer {}".format(self.mod)}, json=self.new_artist)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['artist_id'], artist.id)

    def test_delete_video_w_wrong_token(self):
        print('Testing to Delete one Video in specific with Artist Token: ')
        video = Video(name="")
        video.insert()

        res = self.client().delete('/videos/1',
                                   headers={"Authorization": "Bearer {}".format(self.artist)}, json=self.new_video)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])

    def test_delete_video_w_token(self):
        print('Testing to Delete one Video in specific with Mod Token: ')
        video = Video(name="")
        video.insert()

        res = self.client().delete('/videos/q',
                                   headers={"Authorization": "Bearer {}".format(self.mod)}, json=self.new_video)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['video_id'], video.id)


if __name__ == "__main__":
    unittest.main()
