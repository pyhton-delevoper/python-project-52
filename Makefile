run:
	poetry run python manage.py runserver

db-run:
		sudo service postgresql start

compile-messages:
		poetry run django-admin compilemessages

deploy:
		poetry run python manage.py migrate
		poetry run gunicorn -w 5 --bind 0.0.0.0:$(PORT) task_manager.wsgi:app