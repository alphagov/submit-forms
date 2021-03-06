all:	flake8

refresh:	clean init static migrate load

server:
	python3 manage.py runserver 8808

init:
	pip3 install -r requirements.txt

static:
	python3 manage.py collectstatic --noinput --clear

migrate:	model.svg
	python3 manage.py makemigrations forms && python3 manage.py migrate

load:	data/organisation.tsv
	python3 manage.py load organisation
	python3 manage.py load phase
	python3 manage.py load datatype
	python3 manage.py load inputtype
	python3 manage.py load pagetype
	python3 manage.py loaddata data/list.json
	python3 manage.py loaddata data/item.json
	python3 manage.py loaddata data/list-item.json
	python3 manage.py loaddata data/field.json
	python3 manage.py loaddata data/page.json
	python3 manage.py loaddata data/page-field.json
	python3 manage.py loaddata data/section.json
	python3 manage.py loaddata data/section-page.json
	python3 manage.py loaddata data/form.json
	python3 manage.py loaddata data/form-section.json

save:
	python3 manage.py dumpdata --indent 4 forms.List > data/list.json
	python3 manage.py dumpdata --indent 4 forms.Item > data/item.json
	python3 manage.py dumpdata --indent 4 forms.ListItem > data/list-item.json
	python3 manage.py dumpdata --indent 4 forms.Field > data/field.json
	python3 manage.py dumpdata --indent 4 forms.Page > data/page.json
	python3 manage.py dumpdata --indent 4 forms.PageField > data/page-field.json
	python3 manage.py dumpdata --indent 4 forms.Section > data/section.json
	python3 manage.py dumpdata --indent 4 forms.SectionPage > data/section-page.json
	python3 manage.py dumpdata --indent 4 forms.Form > data/form.json
	python3 manage.py dumpdata --indent 4 forms.FormSection > data/form-section.json

flake8:
	flake8

clean::
	rm -rf explorer/staticfiles
	find . -name '*.pyc' | xargs rm -f
	find . -name '__pycache__' | xargs rm -rf

data/organisation.tsv:	bin/organisations.py
	@mkdir -p cache/page
	python3 bin/organisations.py > $@

model.svg:	forms/models.py
	python3 manage.py graph_models forms -g -o $@

model.pdf:	model.svg
	rsvg-convert -f pdf -o model.pdf model.svg
