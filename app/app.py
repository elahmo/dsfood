from flask import Flask
from pymongo import MongoClient
import csv
import json

app = Flask(__name__)

#load the config from pyfile
#app.config.from_envvar('DSFOOD_CONFIG')
#run it locally for now on
client = MongoClient('mongodb://localhost:27017')

@app.route('/')
def hello_world():
	#CSV to JSON Conversion
	csvfile = open('../datasets/Nutritions/Nutritions.csv', 'r')
	reader = csv.DictReader( csvfile )
	
	#db = client['test-database']
	#collection = db['nutritions']
	#posts = db.posts
			
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
			results.append(row[field])
			#posts.insert_one(row)

	return str(db.collection_names())

if __name__ == '__main__':
    app.run(port=8080)
