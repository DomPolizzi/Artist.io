# FSND capstone

## Artist.io - a place for artists to exist

Nowadays, streaming is all the rage. Introducing a platform for Artists to stream.



**Heroku link:** (https://finnvoid-capstone.herokuapp.com/)

## Getting Started

## Running the server and starting up

First you need to make sure you have Python and Postgres installed on your machine.

Once you have these installed, go to the root directory of the project.

You will then need to install your Dependencies from requirements.txt 

```
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


To run the server, you will need to execute the following commands in your root directory:

```
export FLASK_APP=app.py
export FLASK_ENV=debug
flask run --reload
```


##### Key Dependencies

- [PYTHON](https://www.python.org/)

- [POSTGRES](https://www.postgresql.org/)

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in api.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.



## API DOCUMENTAION

- Artists contain Name, Age, and Style

- Videos contain Title, Date, and Type

## Roles

- Artists
- Mods ( Moderators)

### Artist Role 

 Can:
 Patch:Artists
 Patch:Videos
 Post:Videos

 ### Mod Role

 Can: 
 Delete:Artists 
 Delete:Videos
 Patch:Artists
 Patch:Videos
 Post:Videos

  ## endpoints

- ('/') Default, nothing special

- ('/artists') Artist List in JSON, you can also post no token needed

- ('/artists/<int:id>') single Artist View. You can Patch and Delete with The Mod or Artist Token 

- ('/videos') Videos ( if any availble) return in a JSON List

- ('/add-videos') Post Videos if Artist bearer token exists

- ('/videos/<int:id>') single Video View. You can Patch and Delete with The Mod or Artist Token 

- ('/authorization/url') login page for the Auth0 domain ( how to aquire tokens)


##TESTING

All tests have been executed in postman, see the .json attached
