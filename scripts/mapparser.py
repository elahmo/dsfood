import json
import csv

with open('../app/static/csv/ccg2ons.js') as json_data:
    d = json.load(json_data)


# get the new codes
mapping = {}
for item in d:
	mapping[item['onscode']] = item['CCG']



# print mapping['E16000054']['onscode']
# get the map csv
with open('../app/static/csv/map_health2013.csv', 'rU') as csvfile:
	lines = [l for l in csvfile]

# print lines[15].split(',')[0]
# print mapping[lines[15].split(',')[1]]['code']
for line in lines:
	try:
		code = line.split(',')[0]
		iden = line.split(',')[1]
		newLine = line.replace(code, mapping[iden]['code'])
		print newLine
	except Exception, e:
		print line		