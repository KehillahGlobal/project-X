init:
	pip3 install -r requirements.txt
	touch .env
.PHONY: init

run:
	python3 manage.py runserver
.PHONY: run

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
.PHONY: migrate

clean:
	find . | grep -E "(/__pycache__)" | xargs rm -rf
	find . -name "*.pyc" -exec rm -f {} \;
.PHONY: clean

format:
	./scripts/format.sh
.PHONY: format