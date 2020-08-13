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

        self.artist = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVKNHZEUnhBakREWDhTZkxrei15VCJ9.eyJpc3MiOiJodHRwczovL2Rldi01NmQzY3RuNy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxY2I1OTlkYThmZmEwMDNkMWY4NWQ1IiwiYXVkIjoiY2FwcGVyIiwiaWF0IjoxNTk3Mjg2NTk2LCJleHAiOjE1OTczNzI5OTYsImF6cCI6IlJCQ3JuNlZTRzUzYmN4bmdadlhEYnZOWUR3YmNHbVhRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDphcnRpc3QiLCJwYXRjaDp2aWRlbyIsInBvc3Q6dmlkZW8iXX0.CeMcgkgQJWHshSVw8U6ST6485Rbh95Q4F0xTn8mRYA7SlZaZfIK5Ge2Mj8TmZwx_aIo65xGe0Lokm_XcI2wAVZ_rqJ7hi7-PJcZYV13XATL7_74PH6GzYXDoD5RQ5zB1SGG3rSB4S7nq8rya6xM5hjgsEJXx5U-_4CrBLKfQLFUftufpeKQ94eDGY7-8chvMetjASSe2If6PWvlYqbuwGgq7pt9SYWmmA1vukn6Rf0EVL0R_OJsfc98NyF16yVWXfKX_Nte1zg_rogtMJ1PavRU2Ql4Z3ulaS5znjhVui3CYFUYbUshDe2Aj3jmjjXrIbCPDV0xJ0PIpRA8q2vSi1g'
        self.mod = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVKNHZEUnhBakREWDhTZkxrei15VCJ9.eyJpc3MiOiJodHRwczovL2Rldi01NmQzY3RuNy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxYzlmMzBkYThmZmEwMDNkMWY3NjQ1IiwiYXVkIjoiY2FwcGVyIiwiaWF0IjoxNTk3Mjc1NzU5LCJleHAiOjE1OTczNjIxNTksImF6cCI6IlJCQ3JuNlZTRzUzYmN4bmdadlhEYnZOWUR3YmNHbVhRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0IiwiZGVsZXRlOnZpZGVvIiwicGF0Y2g6YXJ0aXN0IiwicGF0Y2g6dmlkZW8iLCJwb3N0OnZpZGVvIl19.bwjomRmWEnAMfgvgK0HcPNZZdjcbwAg-y5-9x74V1rqvFC3Xc72GmXUNrj2yEpHVgw531vQGcfZDzV1nU7N5njd1ruEa73FddlQ4yHHjfhTa2ellATlbw6uEByDunCU0kg2AFLb6vx058APqSYQGQCDXJZ5uPb8VmDN0j3hxJkVdhrW3PBuS_MGW8iPm9oMVzcmBlfROoLlT7u1ud1mJUn805BkEsH7JSIJG8bI5aQJr_3Kq5cmjmnPA331gtNGrAHldfnSWaPwMZ7YYHUU2QS1lZymS4u-70KcZxrUgo-VY54CcTVgJGaxVFBRlAXfsk1qR-3vJTw6FpxdR5Pqkpw'
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
        del data['artists']['id']
        self.assertEqual(data['artists'], {
                         'name': 'Charlie Brown', 'age': 25, 'style': 'musician'})

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
        del data['videos']['id']
        self.assertEqual(data['videos'], {'title': 'Jazz Theory',
                                          'type': 'Stream', 'date': data['videos']['date']})

    def test_get_video(self):
        print('Testing to check if Videos exist: ')
        res = self.client().get('/videos')
        data = json.loads(res.data)

        videos = Video.query.order_by(Video.id).all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        for video in videos:
            v = next(v for v in data['videos'] if v['id'] == video.id)
            self.assertEqual(v['title'], video.title)
            self.assertEqual(v['type'], video.type)

    def test_get_artist_by_id(self):
        print('Testing to check on one artist in specific: ')

        artist = Artist.query.get(1)

        res = self.client().get('/artists/' +str(artist.id))
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists']['name'], artist.name)

    def test_patch_artist_w_token(self):
        print('Testing to Patch one Video in specific with Mod Token: ')
        artist = Artist(name="Jake Mesa", style="Disk Jockey", age="19")
        artist.insert()

        res = self.client().patch('/artists/' +str(artist.id),
                                  headers={"Authorization": "Bearer {}".format(self.mod)}, json={"style": "magician"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['artists']['style'], 'magician' )

    def test_patch_video_w_token(self):
        print('Testing to Patch one Artist in specific with Mod Token: ')
        video = Video(title="MagicMan", type="tutorial")
        video.insert()

        res = self.client().patch('/videos/' + str(video.id),
                                  headers={"Authorization": "Bearer {}".format(self.mod)}, json={"type": "livestream"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['video']['type'], 'livestream')

    def test_delete_artist_w_token(self):
        print('Testing to Delete one artist in specific Mod Token: ')
        artist = Artist(name="Alex Grey", style="Artist", age="69")
        artist.insert()

        res = self.client().delete('/artists/' + str(artist.id),
                                   headers={"Authorization": "Bearer {}".format(self.mod)})
        deleted_artist = Artist.query.get(artist.id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(deleted_artist, None)

    def test_delete_video_w_wrong_token(self):
        print('Testing to Delete one Video in specific with Artist Token: ')
        video = Video(title="The Giver", type="Movie")
        video.insert()

        res = self.client().delete('/videos/' +  str(video.id),
                                   headers={"Authorization": "Bearer {}".format(self.artist)})

        self.assertEqual(res.status_code, 401)

    def test_delete_video_w_token(self):
        print('Testing to Delete one Video in specific with Mod Token: ')
        video = Video(title="The Giver", type="Movie")
        video.insert()

        res = self.client().delete('/videos/' + str(video.id),
                                   headers={"Authorization": "Bearer {}".format(self.mod)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])


if __name__ == "__main__":
    unittest.main()
