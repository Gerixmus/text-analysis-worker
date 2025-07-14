build:
	docker build -t text-analysis .

run:
	docker run --rm -v data:/app/data text-analysis --in /app/data/input.txt

up:
	docker compose up --build 

down:
	docker compose down --remove-orphans