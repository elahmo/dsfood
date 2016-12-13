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
	dataset = 'dataset_list'
	collection = db[dataset]

	query = collection.find()
	return render_template('index.html', query=query)

#----------------------------------------------------------------
# Inserting Dataset
# Input path and dataset name
# No need to convert csv to JSON
# since flask is smart enough to handle bson file from pymongo
#----------------------------------------------------------------
@app.route('/insert_dataset', methods=['GET', 'POST'])
def insert_dataset():
	error = None
	if request.method == 'POST':
		#'/home/salgadd/dsfood/datasets/Nutritions/Nutritions.csv'
		if request.form['path'] != '' and request.form['dataset'] != '' and request.form['delimiter'] != '':
			file_path = request.form['path']
			dataset = request.form['dataset']
			delimiter = str(request.form['delimiter'])
			dataset_list = db['dataset_list']
			collection = db[dataset]

			csvfile = open(file_path, 'r')
			csv.register_dialect(
				'dataset',
				delimiter = delimiter,)
			reader = csv.DictReader(csvfile, dialect='dataset')

			results = []
			for each in reader:
				results.append(each)

			collection.insert_many(results)
			dataset_list.insert_one({'name': dataset})
			error = 'Insert success'
		else:
			error = 'Empty string'

	return render_template('insert_dataset.html', error=error)

#----------------------------------------------------------------
# Viewing Dataset
# input dataset name to get the data
#----------------------------------------------------------------
@app.route('/view_dataset', methods=['GET', 'POST'])
def view_dataset():
	error = None
	dataset_list = db['dataset_list']
	query_option = dataset_list.find()
	if request.method == 'POST':
		#'/home/salgadd/dsfood/datasets/Nutritions/Nutritions.csv'
		if request.form['dataset'] != '':
			dataset = request.form['dataset']
			collection = db[dataset]

			query = collection.find()
		else:
			query = []
			error = 'Empty string'
	else:
		query = []

	return render_template('view_dataset.html', error=error, query=query, query_option=query_option)

#----------------------------------------------------------------
# Deleting Dataset
# Input dataset name
#----------------------------------------------------------------
@app.route('/delete_dataset', methods=['GET', 'POST'])
def delete_dataset():
	error = None
	dataset_list = db['dataset_list']
	query_option = dataset_list.find()
	if request.method == 'POST':
		#'/home/salgadd/dsfood/datasets/Nutritions/Nutritions.csv'
		if request.form['dataset'] != '':
			dataset = request.form['dataset']
			collection = db[dataset]

			collection.remove()
			dataset_list.remove({'name': dataset})
			error = 'Remove success'
		else:
			error = 'Empty string'

	return render_template('delete_dataset.html', error=error, query_option=query_option)

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


@app.route('/presentation/index')
@app.route('/presentation')
def presentation():
	#get the data from db about health and consumption
	chart_data = {}
	chart_data['health_years'] = []
	chart_data['health_total'] = []
	chart_data['health_male'] = []
	chart_data['health_female'] = []
	chart_data['health_unknown'] = []
	query_health = db['health_diagnosis_gender_years.csv'].find().sort('Year', 1)
	for result in query_health:
		chart_data['health_years'].append(result['Year'])
		chart_data['health_total'].append(result['All persons'].replace(',',''))
		chart_data['health_male'].append(result['Male'].replace(',',''))
		chart_data['health_female'].append(result['Female'].replace(',',''))
		chart_data['health_unknown'].append(result['Unknown'].replace(',',''))

	return render_template('p_index.html', chart_data = chart_data)

@app.route('/presentation/health')
def p_health():
	return render_template('p_health.html')

@app.route('/presentation/price')
def p_price():
	return render_template('p_price.html')

@app.route('/presentation/consumption')
def p_consumtion():
	return render_template('p_consumption.html')

@app.route('/presentation/sugarprice')
def p_sugarprice():
	return render_template('p_sugarprice.html')

@app.route('/presentation/summary')
def p_summary():
	return render_template('p_summary.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
