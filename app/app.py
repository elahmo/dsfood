from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from pymongo import MongoClient
import csv
import json

app = Flask(__name__)

#load the config from pyfile
#app.config.from_envvar('DSFOOD_CONFIG')
#run it locally for now on

client = MongoClient('localhost', 27017)
db = client.dsfood
nutritions = db.nutritions

@app.route('/')
def main_page():
	#session.clear()
	dataset = nutritions.find()
	return render_template('index.html', dataset=dataset)


if __name__ == '__main__':
    app.run(port=8080)
