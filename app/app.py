from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

#load the config from pyfile
app.config.from_envvar('DSFOOD_CONFIG')
client = MongoClient(app.config['MONGO_URI'])

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()