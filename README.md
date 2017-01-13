# dsfood
A GitHub repository for the Data Science final project regarding food, health, and consumtion.

This will be used to store all of our files, meeting notes, data sets and other files.

# Structure

- /meetings (used to store all of our meeting notes)
- /datasets (used to store our datasets, both raw and cleaned)
- /app      (source code for the app)
- /demo     (recording of the app)
- /analysis (some statistical things)
- /documents
- /presentation (pptx for presentation)
- /scripts  (various scripts)


# How to run the app

- have mongo installed, with default credentials, if those are changed, the app has to be updated to run them
- from app dir, run pip install -r requirements
- run the importer script from import/
- python app.py and open localhost:8080

# Commit counts, adjusted for unknown commits
Ahmet	116

Lingga	71

Gerard	32

Chidi	25

Ada	17

total: 261

# Commit convention

So for the commits these are the rules to follow: 

###[folder_concerned][add/mod/del] Explanation 

(Add = adding a file, mod = modification, del = deletion)


# VM Server

Address : svm-sy1n15-comp6235-group.ecs.soton.ac.uk

Note 30/11/16
I've moved our dsfood project to /var/www as it seems to be configured in apache2 instead of running directly with flask.
I've added wsgi and config file in apache2 but still no luck...
Apache2 configuration named dsfood.conf located in /etc/apache2/sites-available

# Layout of the page (@gg)

# Webapp - The sugar Tax

 ## Info to display

Present the Question with graphs and data 
	- explain the Tax and Data they rely on
	- Basic graphs to show the importance of the subject 

Show our research and findings + recommendations 
	- UK region distribution of general sugar consumption VS health issues in those regions
	- UK region distribution of soft drinks consumption VS health issues in those regions
	- Soft drinks prices VS Expenses on soft drinks
	- Soft drinks consumption VS price fluctuations
	- Soft drinks consumption VS health issues
	- historical sugar prices (+$ index for normaisation) VS general sugar consumption
	- historical sugar prices VS soft drinks consumption

/!\ Not forget to add Analytic data on this graphs if relevant

Finish strongly with
	- Conclusion graph on health VS soft drinks prices


## Structure

Either 
 - a long page
 - a multiple pages for the different information
