from pymongo import MongoClient
import csv
import json
import os
from glob import glob
import ntpath


client = MongoClient('localhost', 27017)
db = client.dsfood

#goes through all of the files in the datasets directory
csv_files = [y for x in os.walk('../datasets/Sugar prices') for y in glob(os.path.join(x[0], '*.csv'))]

def filename_helper(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#clear all data first
dataset_list = db.collection_names()
for col in dataset_list:
	db.col.drop()
#do the actual insertion
for csv_file in csv_files:
	try:
		#print csv_file
		file_path = csv_file
		dataset = filename_helper(csv_file)
		delimiter = ',' #change this if your dataset uses something else
		if 'Sugar prices' in file_path or 'US Dollar Index' in file_path:
			delimiter = ';'
		if 'IMF' in file_path:
			delimiter = ','
		dataset_list = db['dataset_list']
		collection = db[dataset]

		csvfile = open(file_path, 'rU')
		csv.register_dialect(
			'dataset',
			delimiter = delimiter,)
		reader = csv.DictReader(csvfile, dialect='dataset')

		results = []
		for each in reader:
			results.append(each)
		#print(results)
		collection.insert_many(results)
		dataset_list.insert_one({'name': dataset})
	except Exception as e:
		print csv_file
		raise e