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

('/') Default, nothing special

GET '/artists'
- Fetches a JSON object with a list of artists in the database.
- Returns: Artists

```
{
  "artists": [
    {
      "age": 25,
      "id": 1,
      "name": "Krishna Rungta",
      "style": "Musician"
    },
    {
      "age": 99,
      "id": 4,
      "name": "Micheal Jackson",
      "style": "Performer"
    },
    {
      "age": 29,
      "id": 2,
      "name": "Sonic",
      "style": "Musician"
    },
    {
      "age": 29,
      "id": 3,
      "name": "Sonic",
      "style": "Musician"
    },
    {
      "age": 99,
      "id": 5,
      "name": "Micheal Jackson",
      "style": "Performer"
    }
  ],
  "success": true
}
```

GET '/videos'
- Fetches a JSON object with a list of videos in the database.
- Returns: videos

```
{
  "success": true,
  "videos": [
    {
      "date": "Thu, 13 Aug 2020 03:01:22 GMT",
      "id": 1,
      "title": "Narwhals",
      "type": "Video"
    },
    {
      "date": "Thu, 13 Aug 2020 03:01:48 GMT",
      "id": 2,
      "title": "Jordan the Magician gets laid",
      "type": "Documentary"
    },
    {
      "date": "Thu, 13 Aug 2020 03:02:07 GMT",
      "id": 3,
      "title": "Applegate in Overwatch",
      "type": "Livestream"
    }
  ]
}
```

POST '/artists'
- Posts a new artist to the database, including the name, age, and style.
- Request Arguments: Requires the arguments: name, age, and style.
- Returns: A artist object with the name, age, and style.
```
{
    "artists": {
        "age": 69,
        "id": 6,
        "name": "Leroy Jenkens",
        "style": "Chef"
    },
    "success": true
}
```

POST '/add-videos'
- Posts a new video to the database, including the title, type, and a Timestamp which is automatically assigned upon insertion. Requires Mod or Artist Token
- Request Arguments: Requires the arguments: title and type.
- Returns: A video object with the title, type, and time created.

```
{
    "success": true,
    "videos": {
        "date": "Thu, 13 Aug 2020 03:02:07 GMT",
        "id": 3,
        "title": "Applegate in Overwatch",
        "type": "Livestream"
    }
}
```

PATCH '/artists/<int:artist_id>'
- Patches an existing artist in the database.
- Request arguments: artist ID, and the key to be updated passed into the body as a JSON object. For example, to update the name for '/artists/3'
- Requires a Bearer Token from Mod or Artist
```
{
    "name": "Shadow"
}
```
- Returns: An Artist object with all details of the specified Artist.
```
{
    "artists": {
        "age": 29,
        "id": 3,
        "name": "Shadow",
        "style": "Musician"
    },
    "success": true
}
```
PATCH '/videos/<int:video_id>'
- Patches an existing video in the database.
- Request arguments: video ID, and the key to be updated passed into the body as a JSON object. For example, to update the title and type for '/videos/2'
- Requires a Bearer Token from Mod or Artist
```
{
    "title": "BabyShark (Singalong)",
    "type": "Video"
}
```
- Returns: An Artist object with all details of the specified Artist.
```
{
    "success": true,
    "video": {
        "date": "Thu, 13 Aug 2020 03:01:48 GMT",
        "id": 2,
        "title": "BabyShark (Singalong)",
        "type": "Video"
    }
}
```
DELETE '/artists/<int:artist_id>'
- Deletes an artist in the database via the DELETE method and using the artist id.
- Request argument: Artist id, included as a parameter following a forward slash (/).
- Returns: ID for the deleted Artist and status code of the request.
- Requires a Mod Bearer token
```
{
    "delete": 3,
    "success": true
}
```

DELETE '/videos/<int:video_id>'
- Deletes an video in the database via the DELETE method and using the video id.
- Request argument: Video id, included as a parameter following a forward slash (/).
- Returns: ID for the deleted Video and status code of the request.
- Requires a Mod Bearer token, Artist is not allowed
```
{
    "delete": 3,
    "success": true
}
```

## TESTING

To run the unittests
```
createdb capstonetest
python3 test_app.py
```
All tests have been executed in postman aswell, see the .json attached
