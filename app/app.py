from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

#load the config from pyfile
#app.config.from_envvar('DSFOOD_CONFIG')
#run it locally for now on
client = MongoClient('mongodb://localhost:27017/test')

@app.route('/')
def hello_world():
	db = client.test.collection
	#data = db.find()
	#posts = db.posts
	#post = {'author':'ahmet the man', 'text': 'This is just a sample text, I wonder where she is btw!'}
	#post_id = posts.insert_one(post)
	return str(db)

if __name__ == '__main__':
    app.run(port=8080)
