# commands
.PHONY: env
env:
	source .venv/bin/activate

.PHONY: deact
deact:
	deactivate

# Django commands
# Run Django server
.PHONY: server
server:
	python -m manage runserver 8005

# Run Django migrations
.PHONY: migrate
migrate:
	python -m manage makemigrations; python -m manage migrate
