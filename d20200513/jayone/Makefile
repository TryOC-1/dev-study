VENV:=../../venv
PYTHON:=$(VENV)/bin/python

pyramid:
	$(PYTHON) wsgi_server.py pyramidapp:app

flask:
	$(PYTHON) wsgi_server.py flaskapp:app

django:
	$(PYTHON) wsgi_server.py djangoapp:app

simple:
	$(PYTHON) wsgi_server.py simple_framework:app