# Makefile for backend tasks

.PHONY: install test lint format run

install:
	python -m venv venv && source venv/bin/activate && pip install -r requirements.txt

test:
	pytest tests/

lint:
	flake8 . --exclude=venv

format:
	black . && isort .

run:
	python app.py
