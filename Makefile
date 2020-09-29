build:
	docker build --force-rm $(option) -t djangotest_website_test:latest .

build-prod:
	$(make) build option="--target production"

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd)