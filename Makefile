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

load:	data/organisation.tsv
	python3 manage.py load organisation
	python3 manage.py load phase
	python3 manage.py load datatype
	python3 manage.py load inputtype

flake8:
	flake8

clean::
	rm -rf explorer/staticfiles
	find . -name '*.pyc' | xargs rm -f
	find . -name '__pycache__' | xargs rm -rf

data/organisation.tsv:	bin/organisations.py
	@mkdir -p cache/page
	python3 bin/organisations.py > $@

