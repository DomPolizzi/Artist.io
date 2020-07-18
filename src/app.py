from flask import Flask
from api import APP

app = APP

if __name__ == '__main__':
    app.run()