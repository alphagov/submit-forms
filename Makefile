all:	flake8

refresh:	clean init static migrate load

server:
	python3 manage.py runserver 8808

init:
	pip3 install -r requirements.txt

static:
	python3 manage.py collectstatic --noinput --clear

migrate:
	python3 manage.py makemigrations forms
	python3 manage.py migrate

load:
	python3 manage.py load organisations
	python3 manage.py load forms

flake8:
	flake8

clean::
	rm -rf explorer/staticfiles
	find . -name '*.pyc' | xargs rm -f
	find . -name '__pycache__' | xargs rm -rf
