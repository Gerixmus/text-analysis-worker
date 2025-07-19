GIT_TAG=$(shell git describe --tags --abbrev=0)
TAG=$(subst v,,$(GIT_TAG))

print:
	@echo $(TAG)

build:
	docker build -t text-analysis-worker:$(TAG) .

run:
	docker run --rm -v data:/app/data text-analysis-worker --in /app/data/input.txt

up:
	docker compose up --build 

down:
	docker compose down --remove-orphans