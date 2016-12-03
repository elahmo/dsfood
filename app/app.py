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


@app.route('/insert_dataset')
def insert_dataset():
	#CSV to JSON Conversion
	csvfile = open('/home/salgadd/dsfood/datasets/Nutritions/Nutritions.csv', 'r')
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
	dataset = nutritions.find()

	return render_template('insert_dataset.html', dataset=dataset)


if __name__ == '__main__':
    app.run(port=8080)
