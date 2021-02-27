Sparesnmechs
============
This is the backend API server for a Mobile first platform that connects car owners, 
spare part dealers and mechanics.

How to install the project
--------------------------
Prerequisites
~~~~~~~~~~~~~
Make sure you have the following before beginning:

	- python3-dev
	- git
	- pip
	- virtualenv
	- postgresql

Cloning from Github
~~~~~~~~~~~~~~~~~~~
From your terminal got to the directory you want to clone your project into.

.. code:: bash

	$ cd path/to/your/directory

Clone the project

.. code:: bash

	$ cd git clone git@github.com:sparesnmechs/sparesnmechs.git

Set up the environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create a env.sh file in your parent project directory

.. code:: bash

	$ cd path/to/your/directory/sparesnmechs
	$ touch env.sh

Add these environment variables to your ``env.sh`` file:

.. code:: bash

	#!/usr/bin/env bash

	export SECRET_KEY="your-secret-key"
	export DEBUG="true"  #For development only
	export DB_NAME="db_name"
	export DB_USER="db_user"
	export DB_PASS="db_pass"
	export DB_HOST="127.0.0.1"
	export DB_PORT="5432"

Setting up the projects dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Navigate into the projects directory from the terminal.

.. code:: bash

	$ cd path/to/your/directory/sparesnmechs

Create a virtual environment for your project

.. code:: bash

	$ python3 -m venv name-of-your-virtualenv

Activate your virtual environment.

.. code:: bash

	$ source name-of-your-virtualenv/bin/activate

Source your env.sh file.

.. code:: bash

	$ source env.sh

Install the requirements.

.. code:: bash

	$(name-of-your-virtualenv) pip install -r requirements.txt

Running and testing the project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create a ``postgresql`` database with the information in ``env.sh``.

Make the initial migrations:

.. code:: bash

	(name-of-your-virtualenv)$ ./manage.py makemigrations
	(name-of-your-virtualenv)$ ./manage.py migrate

To run the project:

.. code:: bash
	
	$(name-of-your-virtualenv) ./manage.py runserver # the information below will be displayed if everything is okay
	Performing system checks...

	System check identified no issues (0 silenced).
	December 7, 2019 - 18:55:56
	Django version 3.0, using settings 'config.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.
	
To test the project:

.. code:: bash

	$(name-of-your-virtualenv) tox -r # This will run all the tests in the project

Credits
-------
Developed by **Kenneth Mathenge**
