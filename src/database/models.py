from sqlalchemy import Column, String, Integer, create_engine, Date
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

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
    # this one -v
    db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
    You will need to comment the above db.create_all()
'''
# for this one -v
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
'''

class Artist(db.Model):  
  __tablename__ = 'Artist'

  id = Column(Integer(), primary_key=True)
  name = Column(String())
  age = Column(Integer())
  style = Column(String())

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
  
  #save to call later?
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