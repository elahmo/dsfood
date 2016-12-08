from pymongo import MongoClient
import csv
import json
import os
from glob import glob
import ntpath


client = MongoClient('localhost', 27017)
db = client.dsfood

#goes through all of the files in the datasets directory
csv_files = [y for x in os.walk('../datasets/Health') for y in glob(os.path.join(x[0], '*.csv'))]

def filename_helper(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#do the actual insertion
for csv_file in csv_files:
	try:
		print csv_file
		file_path = csv_file
		dataset = filename_helper(csv_file)
		delimiter = ',' #change this if your dataset uses something else
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
		print(results)
		collection.insert_many(results)
		dataset_list.insert_one({'name': dataset})
	except Exception as e:
		raise e
