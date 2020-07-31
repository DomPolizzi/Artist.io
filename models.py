import os
import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
import json


database_path = os.environ.get('HEROKU_POSTGRESQL_ROSE_URL')


if not database_path:
    database_name = "capstone"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #db.drop_all()
    db.create_all()

'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
'''



#Models:

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = Column(Integer(), primary_key=True)
    name = Column(String(80))
    age = Column(Integer())
    style = Column(String(50))
    videos_rel = relationship("Video")

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id

  '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database

  '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
  '''

    def update(self):
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "style": self.style
        }


class Video(db.Model):
    __tablename__ = 'Video'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    date = Column(DateTime, default=datetime.datetime.utcnow)
    # Video type, Stream or Saved Video
    type = Column(String())
    artist_id = Column(Integer, ForeignKey('Artist.id'))


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "type": self.type
        }


    def __repr__(self):
        return json.dumps(self.short())
