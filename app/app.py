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

	chart_data['ages_years'] = []
	chart_data['ages_all'] = []
	chart_data['ages_16'] = []
	chart_data['ages_24'] = []
	chart_data['ages_34'] = []
	chart_data['ages_44'] = []
	chart_data['ages_54'] = []
	chart_data['ages_64'] = []
	chart_data['ages_74'] = []
	chart_data['ages_over'] = []
	chart_data['ages_unknown'] = []

	query_age = db['health_diagnosis_gender_years_age.csv'].find().sort('Year', 1)
	for result in query_age:
		chart_data['ages_years'].append(result['Year'].replace(',',''))
		chart_data['ages_all'].append(result['All ages'].replace(',',''))
		chart_data['ages_16'].append(result['Under 16'].replace(',',''))
		chart_data['ages_24'].append(result['16 to 24'].replace(',',''))
		chart_data['ages_34'].append(result['35 to 44'].replace(',',''))
		chart_data['ages_44'].append(result['35 to 44'].replace(',',''))
		chart_data['ages_54'].append(result['45 to 54'].replace(',',''))
		chart_data['ages_64'].append(result['55 to 64'].replace(',',''))
		chart_data['ages_74'].append(result['65 to 74'].replace(',',''))
		chart_data['ages_over'].append(result['75 and over'].replace(',',''))
		chart_data['ages_unknown'].append(result['Unknown'].replace(',',''))

	return render_template('p_index.html', chart_data = chart_data)

@app.route('/presentation/health')
def p_health():
	#get the data from db about health and consumption
	chart_data = {}
	years = ['2006','2007','2008','2009','2010','2011','2012','2013','2014']
	chart_data['England'] = {}
	chart_data['England']['obesity'] = []
	chart_data['England']['consumption'] = []
	chart_data['England']['hc'] = []
	chart_data['England']['lc'] = []
	chart_data['North_East'] = {}
	chart_data['North_East']['obesity'] = []
	chart_data['North_East']['consumption'] = []
	chart_data['North_East']['hc'] = []
	chart_data['North_East']['lc'] = []
	chart_data['North_West'] = {}
	chart_data['North_West']['obesity'] = []
	chart_data['North_West']['consumption'] = []
	chart_data['North_West']['hc'] = []
	chart_data['North_West']['lc'] = []
	chart_data['Yorkshire_and_The_Humber'] = {}
	chart_data['Yorkshire_and_The_Humber']['obesity'] = []
	chart_data['Yorkshire_and_The_Humber']['consumption'] = []
	chart_data['Yorkshire_and_The_Humber']['hc'] = []
	chart_data['Yorkshire_and_The_Humber']['lc'] = []
	chart_data['East_Midlands'] = {}
	chart_data['East_Midlands']['obesity'] = []
	chart_data['East_Midlands']['consumption'] = []
	chart_data['East_Midlands']['hc'] = []
	chart_data['East_Midlands']['lc'] = []
	chart_data['West_Midlands'] = {}
	chart_data['West_Midlands']['obesity'] = []
	chart_data['West_Midlands']['consumption'] = []
	chart_data['West_Midlands']['hc'] = []
	chart_data['West_Midlands']['lc'] = []
	chart_data['East'] = {}
	chart_data['East']['obesity'] = []
	chart_data['East']['consumption'] = []
	chart_data['East']['hc'] = []
	chart_data['East']['lc'] = []
	chart_data['London'] = {}
	chart_data['London']['obesity'] = []
	chart_data['London']['consumption'] = []
	chart_data['London']['hc'] = []
	chart_data['London']['lc'] = []
	chart_data['South_East'] = {}
	chart_data['South_East']['obesity'] = []
	chart_data['South_East']['consumption'] = []
	chart_data['South_East']['hc'] = []
	chart_data['South_East']['lc'] = []
	chart_data['South_West'] = {}
	chart_data['South_West']['obesity'] = []
	chart_data['South_West']['consumption'] = []
	chart_data['South_West']['hc'] = []
	chart_data['South_West']['lc'] = []
	query_consumption = db['ObesitySoftDRinks_Caloric_NonCaloric.csv'].find().sort('Year', 1)
	for result in query_consumption:
		chart_data[result['region']]['obesity'].append(float(result['obesity'].replace('.','').replace(',', '.')))
		chart_data[result['region']]['consumption'].append(float(result['consumption'].replace('.','').replace(',', '.')))
		chart_data[result['region']]['hc'].append(float(result['caloric'].replace('.','').replace(',', '.')))
		chart_data[result['region']]['lc'].append(float(result['non-caloric'].replace('.','').replace(',', '.')))
	return render_template('p_health.html', chart_data=chart_data, years=years)

@app.route('/presentation/consumption')
def p_consumtion():
	chart_data = {}
	# consumption, total household
	chart_data['consumption_years'] = []
	chart_data['consumption_years2'] = []
	chart_data['consumption_1'] = []
	chart_data['consumption_2'] = []
	chart_data['consumption_3'] = []
	chart_data['consumption_4'] = []
	chart_data['consumption_5'] = []
	chart_data['consumption_7'] = []
	chart_data['consumption_8'] = []
	chart_data['consumption_9'] = []
	chart_data['consumption_10'] = []
	chart_data['consumption_11'] = []
	query_consumption = db['AllFoodExpenses.csv'].find().sort('Year', 1)
	for result in query_consumption:
		chart_data['consumption_years'].append(result['Year'])
		chart_data['consumption_1'].append(result['Soft drinks'].replace('.',''))
		chart_data['consumption_2'].append(result['Soft drinks c hc'])
		chart_data['consumption_3'].append(result['Soft drinks nc hc'])
		chart_data['consumption_4'].append(result['Soft drinks c lc'])
		chart_data['consumption_5'].append(result['Soft drinks nc lc'])

	# consumption, eating out expenses
	chart_data['eatingout_years'] = []
	chart_data['eatingout_1'] = []
	chart_data['eatingout_2'] = []
	chart_data['eatingout_3'] = []
	chart_data['eatingout_4'] = []
	chart_data['eatingout_5'] = []
	query_consumption = db['TotalExpensesEatingOutAndHousehold.csv'].find().sort('Year', 1)
	for result in query_consumption:
		chart_data['eatingout_years'].append(result['Year'])
		chart_data['eatingout_1'].append(result['Soft drinks'].replace('.',''))
		chart_data['eatingout_2'].append(result['Soft drinks c hc'])
		chart_data['eatingout_3'].append(result['Soft drinks nc hc'])
		chart_data['eatingout_4'].append(result['Soft drinks c lc'])
		chart_data['eatingout_5'].append(result['Soft drinks nc lc'])

	query_consumption2 = db['QuantitySugarHousehold.csv'].find().sort('Year', 1)
	for result in query_consumption2:
		chart_data['consumption_years2'].append(result['Year'])
		chart_data['consumption_7'].append(result['Soft drinks'].replace('.',''))
		chart_data['consumption_8'].append(result['Soft drinks c hc'])
		chart_data['consumption_9'].append(result['Soft drinks nc hc'])
		chart_data['consumption_10'].append(result['Soft drinks c lc'])
		chart_data['consumption_11'].append(result['Soft drinks nc lc'])

	return render_template('p_consumption.html', chart_data = chart_data)

@app.route('/presentation/sugarprice')
def p_sugarprice():
	chart_data = {}
	# monhtly price
	chart_data['price_date'] = []
	chart_data['price_1'] = []
	chart_data['normalised_date'] = []
	chart_data['normalised_1'] = []
	normalisation = {}

	# monhtly price, normalised
	query_normalisation = db['usdindex_10_16_monthly.csv'].find()
	initialValue = 80.44

	for result in query_normalisation:
		normalisation[result['Date']] = float(result[' Index'])/initialValue

	query_monthly = db['monthly_sugar_price_10_16.csv'].find().sort('Date', 1)
	for result in query_monthly:
		chart_data['price_date'].append(result['Date'])
		chart_data['price_1'].append(float(result['Price']))
		chart_data['normalised_date'].append(result['Date'])
		chart_data['normalised_1'].append(float(result['Price'])*normalisation[result['Date']])

	return render_template('p_sugarprice.html', chart_data = chart_data)

@app.route('/presentation/analysis')
def p_analysis():
	return render_template('p_analysis.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
