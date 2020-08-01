# FSND capstone

## Artist.io - a place for artists to exist

Nowadays, streaming is all the rage. IOntroducing a platform for Artists to stream.


**Heroku link:** (https://finnvoid-capstone.herokuapp.com/)

## Getting Started

### Installing Dependencies

pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in api.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

To run the server, execute:

```
export FLASK_APP=app.py
export FLASK_ENV=debug
flask run --reload
```
## Artist.io Models

- Artists contain Name, Age, and Style

- Videos contain Title, Date, and Type

## Roles

- Artists
- Mods ( Moderators)

### Artist Role 

 Can Patch Artist, Patch Video, and Post Videos

 ### Mod Role

 Can Delete Artists and Videos, and everything an Artist can

  ## endpoints

-  ('/') Default, nothing special

- ('/artists') Artist List in JSON, you can also post if token permits

- ('/artists/<int:id>') single Artist Patch, view and Delete methods allowed 

- ('/videos') Videos ( if any availble) return in a JSON List

- ('/add-videos') Post Videos if Artist bearer token exists

- ('/videos/<int:id>') single video Patch, view, and delete if Token exists

- ('/authorization/url') login page for the Auth0 domain ( how to aquire tokens)

##TESTING

All tests have been executed in postman, see the .json attached
