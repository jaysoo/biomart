BioMart website (biomart.org)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> core settings
>>>>>>> trunk
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


Checkout from svn and deploy
----------------------------

1. Checkout trunk from SVN

    svn co https://code.oicr.on.ca/svn/dcc_dev/biomart_django/trunk biomart_django_trunk

2. Sync data (follow instructions, and make sure you create a superuser)

    cd biomart_django_trunk/biomart
    python manage.py syncdb

3. Migrate models

    python manage.py migrate 

4. Run Gunicorn

    gunicorn_django -c [svn_trunk]/biomart/gunicorn_config.py [svn_trunk]/biomart/settings.py

5. Load some fixtures

You should now have a dummy server running on http://localhost:9997. The admin URL is 
http://localhost:9997/admin (login using the superuser account you created earlier).

