from flask import Flask
from pymongo import MongoClient
import csv
import json

app = Flask(__name__)

#load the config from pyfile
#app.config.from_envvar('DSFOOD_CONFIG')
#run it locally for now on
client = MongoClient('mongodb://localhost:27017/test')

@app.route('/')
def hello_world():
	#CSV to JSON Conversion
	csvfile = open('../datasets/Nutritions/Nutritions.csv', 'r')
	reader = csv.DictReader( csvfile )
	
	db = client.test

	return str('hai')

if __name__ == '__main__':
    app.run(port=8080)
