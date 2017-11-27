all:	flake8

refresh:	clean init static migrate load

server:
	python3 manage.py runserver 8808

init:
	pip3 install -r requirements.txt

static:
	python3 manage.py collectstatic --noinput --clear

migrate:
	python3 manage.py makemigrations forms && python3 manage.py migrate

load:	data/organisation.tsv
	python3 manage.py load organisation
	python3 manage.py load phase
	python3 manage.py load datatype
	python3 manage.py load inputtype
	python3 manage.py loaddata data/list.json
	python3 manage.py loaddata data/field.json
	python3 manage.py loaddata data/question.json
	python3 manage.py loaddata data/question-field.json
	python3 manage.py loaddata data/section.json
	python3 manage.py loaddata data/section-question.json
	python3 manage.py loaddata data/form.json
	python3 manage.py loaddata data/form-section.json

save:
	python3 manage.py dumpdata --indent 4 forms.List forms.Item > data/list.json
	python3 manage.py dumpdata --indent 4 forms.Field > data/field.json
	python3 manage.py dumpdata --indent 4 forms.Question > data/question.json
	python3 manage.py dumpdata --indent 4 forms.QuestionField > data/question-field.json
	python3 manage.py dumpdata --indent 4 forms.Section > data/section.json
	python3 manage.py dumpdata --indent 4 forms.SectionQuestion > data/section-question.json
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

