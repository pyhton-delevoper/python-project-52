run:
		poetry run python manage.py runserver

migrations:
		poetry run python3 manage.py makemigrations
		poetry run python3 manage.py migrate

compile-messages:
		poetry run django-admin compilemessages

PORT ?= 8000
deploy:
		poetry run python3 manage.py migrate
		poetry run gunicorn -w 5 --bind 0.0.0.0:$(PORT) task_manager.wsgi

lint:
		poetry run flake8 task_manager

reset-db:
		poetry run python manage.py reset_db

start-db:
		sudo service postgresql start

shell:
		poetry run python manage.py shell_plus