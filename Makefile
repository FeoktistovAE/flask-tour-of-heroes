start:
	poetry run flask --app tour_of_heroes.start run
migrations:
	alembic revision --autogenerate
migrate:
	alembic upgrade head
lint:
	poetry run flake8 tour_of_heroes