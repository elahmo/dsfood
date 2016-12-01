# dsfood
A GitHub repository for the Data Science final project regarding food, health, and consumtion.

This will be used to store all of our files, meeting notes, data sets and other files.

# Structure

- /meetings (used to store all of our meeting notes)
- /datasets (used to store our datasets, both raw and cleaned)
- /app      (source code for the app)

# Commit convention

So for the commits these are the rules to follow: 

###[folder_concerned][add/mod/del] Explanation 

(Add = adding a file, mod = modification, del = deletion)


# VM Server

Address : svm-sy1n15-comp6235-group.ecs.soton.ac.uk
User    : user
Pass    : awesomeGroup2

Note 30/11/16
I've moved our dsfood project to /var/www as it seems to be configured in apache2 instead of running directly with flask.
I've added wsgi and config file in apache2 but still no luck...
Apache2 configuration named dsfood.conf located in /etc/apache2/sites-available