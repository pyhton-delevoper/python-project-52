run:
		poetry run python manage.py runserver

migrations:
		poetry run python3 manage.py makemigrations
		poetry run python3 manage.py migrate

compile-messages:
		poetry run django-admin compilemessages

deploy:
		poetry run python3 manage.py migrate
		poetry run gunicorn -w 5 --bind 0.0.0.0:$(PORT) task_manager.wsgi:app