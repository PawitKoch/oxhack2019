# OxHack 2019 Flask Carbon Capture Project (w/ Flask boilerplate code)

## Features

- [x] Image Upload, with computer vision prediction handler (Azure Cognitive Services).
- [x] Prediction table plotter with plotly, pandas on results page.
- [x] User account sign up, sign in, password reset, all through asynchronous email confirmation.
- [x] Python 3.x compliant.
- [x] Virtual environment example.
- [x] Digital Ocean deployment example.
- [x] Logging.

## Structure

I did what most people recommend for the application's structure. Basically, everything is contained in the `app/` folder.

- There you have the classic `static/` and `templates/` folders. The `templates/` folder contains macros, error views and a common layout.
- I added a `views/` folder to separate the user and the website logic, which could be extended to the the admin views.
- The same goes for the `forms/` folder, as the project grows it will be useful to split the WTForms code into separate files.
- The `models.py` script contains the SQLAlchemy code, for the while it only contains the logic for a `users` table.
- The `toolbox/` folder is a personal choice, in it I keep all the other code the application will need.
- Management commands should be included in `manage.py`. Enter `python manage.py -?` to get a list of existing commands.
- I added a Makefile for setup tasks, it can be quite useful once a project grows.


## Setup

### Vanilla

- Install the requirements and setup the development environment.

	`make install && make dev`

- Create the database.

	`python manage.py initdb`

- Run the application.

	`python manage.py runserver`

- Navigate to `localhost:5000`.


### Virtual environment

``
pip install virtualenv
virtualenv venv
venv/bin/activate
make install
make dev
python manage.py initdb
python manage.py runserver
``
