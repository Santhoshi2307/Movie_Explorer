build:
	docker compose build

# Start services
up:
	docker compose up -d

# Stop services
down:
	docker compose down

# Rebuild services
rebuild:
	docker compose down
	docker compose build
	docker compose up -d

# Run backend tests using pytest
test-backend:
	docker compose run --rm backend pytest

# Run frontend tests using Jest
test-frontend:
	docker compose run --rm frontend npm run test:ci

# Run all tests (backend + frontend)
test: test-backend test-frontend

# Lint backend (flake8) and frontend (eslint)
lint-backend:
	docker compose run --rm backend flake8 .

lint-frontend:
	docker compose run --rm frontend npm run lint

lint: lint-backend lint-frontend

# Show backend logs
logs:
	docker compose logs -f backend

# Remove containers, volumes
clean:
	docker compose down -v --remove-orphans

# Open Swagger Docs
swagger:
	open http://localhost:5000/apidocs