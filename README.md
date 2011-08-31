BioMart website (biomart.org)
=============================

Both the Django project and default Apache configuration files
are in this repo.

You will need at least Python 2.5 to run the application server.

[Gunicorn](http://gunicorn.org/) is the recommended method of deploying the application 
server. You should be running either [Apache](http://apache.org/) or 
[nginx](http://nginx.org), and proxying requests to Gunicorn.


pip and virualenv
-----------------

It is recommended that you use `pip` and `virtualenv` to install the required Python packages.

Please see [PyPI](http://pypi.python.org/) to install `easy_install` first. Then install 
`pip` and `virtualenv` with `easy_install pip virtualenv`. (Note: you may need to use `sudo`)

Assuming you have Python 2.7, simply execute these commands:

    wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
    sh setuptools-0.6c11-py2.7.egg
    sudo easy_isntall pip virtualenv


Activating virtualenv
---------------------

Now that `virualenv` is installed, create a new virtual environment and activate it.

    mkdir -p ~/env
    virtualenv ~/env/biomart
    source ~/env/biomart/bin/activate

(Note: you can deactivate the environment with the `deactivate` command).


Installing required Python modules
----------------------------------

These are the modules required to run the BioMart server. The tested version numbers are 
listed in parentheses, although newer versions of all the modules should be okay to use.

* pil
* mysql-python
* python-memcached
* gunicorn 
* django 
* django-grappelli
* django-filebrowser
* south

To install these packages, run this command:

    pip install pil mysql-python python-memcached gunicorn django django-grappelli django-filebrowser south


Checkout from SVN and deploy
----------------------------

1. Checkout trunk from SVN

        svn co https://code.oicr.on.ca/svn/dcc_dev/biomart_django/trunk biomart_django_trunk

2. Sync data (follow instructions, and make sure you create a superuser)

        cd biomart_django_trunk/biomart
        python manage.py syncdb

3. Migrate models

        python manage.py migrate 

4. Load some fixtures

        python manage.py loaddata fixtures/core.json fixtures/flatpages.json

5. Run Gunicorn

        gunicorn_django -c [svn_trunk]/biomart/gunicorn_config.py [svn_trunk]/biomart/settings.py

You should now have a dummy server running on http://localhost:9997. The admin URL is 
http://localhost:9997/admin (login using the superuser account you created earlier).

You can stop the Gunicorn daemon processes by killing the master process. The PID file should 
created under the directory in which you ran the `gunicorn_django` command.

    kill `cat gunicorn.pid`


Local settings
--------------

Database connection and memcached info should go into a file called `local_settings.py`, in the
same folder as settings.py. We don't include these settings in the SVN repo because they differ
between environments.

If you are using MySQL, you will need a setting similar to the below:

    # Make sure all settings are correct below!
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'biomart',                      # Or path to database file if using sqlite3.
            'USER': 'username',                      # Not used with sqlite3.
            'PASSWORD': 'password',                  # Not used with sqlite3.
            'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

For memcached settings, use the following:

    # This assumes default memcached port of 11211 running on localhost
    # If this is not correct, please change it!
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

Please see the Django documentation for more information (https://docs.djangoproject.com/en/1.3/topics/settings/).

Relaunch the Gunicorn processes to load the new settings. You will need to redo steps 2-4 from the previous 
section in order to load the data into a fresh database.


Serving behind HTTP server
--------------------------

Note that static files are not served by the Django server (unless `DEBUG=True` in the settings). The static files
need to be served by an HTTP server (Apache or nginx). Default Apache configs are under `[svn_trunk]/apache/conf/httpd.conf`.

Please make sure you update all the paths in `httpd.conf` so that they point actual paths on the filesystem.

To run an Apache server with the config file, this command:

    apache2 -d [svn_trunk]/apache2 -f conf/httpd.conf -k start


If `apache2` is not on the PATH, use the full path.

e.g.

    /usr/sbin/apache2 -d /u/jhsu/code/biomart.org/apache2 -f conf/httpd.conf -k start
