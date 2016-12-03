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

#index.html
@app.route('/')
def main_page():
	dataset = 'nutritions'
	collection = db[dataset]

	query = collection.find()
	return render_template('index.html', query=query)

#----------------------------------------------------------------
# Inserting Dataset
# No need to convert csv to JSON
# since flask is smart enough to handle bson file from pymongo
#----------------------------------------------------------------
@app.route('/insert_dataset')
def insert_dataset():
	file_path = '/home/salgadd/dsfood/datasets/Nutritions/Nutritions.csv'
	dataset = 'nutritions'
	collection = db[dataset]

	csvfile = open(file_path, 'r')
	reader = csv.DictReader( csvfile )

	header = [
		"Food Code",
		"Food Name",
		"Description",
		"Group",
		"Previous",
		"Main data references",
		"Footnote",
		"Water (g)",
		"Total nitrogen (g)",
		"Protein (g)",
		"Fat (g)",
		"Carbohydrate (g)",
		"Energy (kcal) (kcal)",
		"Energy (kJ) (kJ)",
		"Starch (g)",
		"Oligosaccharide (g)",
		"Total sugars (g)",
		"Glucose (g)",
		"Galactose (g)",
		"Fructose (g)",
		"Sucrose (g)",
		"Maltose (g)",
		"Lactose (g)",
		"Alcohol (g)",
		"NSP (g)",
		# AOAC fibre (g),
		# Satd FA /100g FA (g),
		# Satd FA /100g fd (g),
		# n-6 poly /100g FA (g),
		# n-6 poly /100g food (g),
		# n-3 poly /100g FA (g),
		# n-3 poly /100g food (g),
		# cis-Mono FA /100g FA (g),
		# cis-Mono FA /100g Food (g),
		# Mono FA/ 100g FA (g),
		# Mono FA /100g food (g),
		# cis-Polyu FA /100g FA (g),
		# cis-Poly FA /100g Food (g),
		# Poly FA /100g FA (g),
		# Poly FA /100g food (g),
		# Sat FA excl Br /100g FA (g),
		# Sat FA excl Br /100g food (g),
		# Branched chain FA /100g FA (g),
		# Branched chain FA /100g food (g),
		# Trans FAs /100g FA (g),
		# Trans FAs /100g food (g),
		"Cholesterol (mg)"];

	results = []
	for each in reader:
		row = {}
		for field in header:
			row[field] = each[field]
		results.append(row)

	#nutritions.insert_many(results)
	query = collection.find()

	return render_template('insert_dataset.html', query=query)

#login, still dummy with user/pass admin/admin
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
        #if request.form['username'] != app.config['USERNAME']:
		if request.form['username'] != 'admin':
			error = 'Invalid username'
        #elif request.form['password'] != app.config['PASSWORD']:
		elif request.form['password'] != 'admin':
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('main_page'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('main_page'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(port=8080)
