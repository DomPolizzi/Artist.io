import os
from sqlalchemy import Column, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
import json


database_path = os.environ.get('DATABASE_URL')

if not database_path:
    database_name = "capstone"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)


db = SQLAlchemy()
moment = Moment()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    moment.app = app
    db.init_app(app)
    db.create_all()


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()



#Models:

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(Integer(), primary_key=True)
    name = db.Column(String(80))
    age = db.Column(Integer())
    style = db.Column(String(50))

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
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'style': self.style
        }


class Video(db.Model):
    __tablename__ = 'Video'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    date = Column(Date, index=True)
    # Video type, Stream or Saved Video
    type = Column(Integer())
    # add later
    # artist =

    # save to call later?
    #qry = DBSession.query(User).filter(User.date.between('1985-01-17', '1988-01-17'))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
