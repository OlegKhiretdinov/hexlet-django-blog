start:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

test: migrate
	python3 manage.py test tests/

console:
	python3 manage.py shell