run:
	poetry run python manage.py runserver
db-run:
	sudo service postgresql start

compile-messages:
	poetry run django-admin compilemessages