# dsfood
A GitHub repository for the final project in Foundations of Data Science (COMP6235). The project was performed during Fall 2016 at University of Southampton. The theme for the project was about food.

The repository contrains all of files that were created during the work, including backend and frontend for the application, meeting notes, datasets and scripts to parse data, presentation and demonstration, and other files.

# Structure

- /analysis 	(statistics)
- /app      	(source code for the app)
- /datasets 	(used to store our datasets, both raw and cleaned)
- /demo     	(recording of the app)
- /meetings 	(used to store all of our meeting notes)
- /presentation	(pptx for presentation)
- /scripts	(various scripts)

# Technical details

The application backend is made with Python flask framework, and has two components:

- backend, used for managing of the datasets that are loaded in the app
- frontend, the presentation layer, showing the interactive map and other things relevant to the project

# Datasets

The following datasets are used in the realisation of this project:

- [Consumption](datasets/Consumption)
- [Health](datasets/Health)
- [Healthy_Living_Data](datasets/Healthy_Living_Data)
- [Nutritions](datasets/Nutritions)
- [Sugar_prices](datasets/Sugar_prices)
- [US_Dollar_Index](datasets/US_Dollar_Index)

Each of the datasets has a corresponding description and source listed in the root directory.


# How to run the app

- have mongo installed, with default credentials, if those are changed, the app has to be updated to run them
- from app dir, run `pip install -r requirements`
- run the importer script from import/
- `python app.py` and then browse the app at localhost:8080


# Commit convention

For the naming of the commits, to keep things sane, these are the rules to follow: 

###[folder_concerned][add/mod/del] Explanation 

(add = adding a file, mod = modification, del = deletion)
