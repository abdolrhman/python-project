# Python Task
A simple project for managing products, categories, and reviews using FastAPI.

## 0. About

The **Python Task** project is a simplified API built with FastAPI for managing products, categories, and reviews. It leverages modern technologies such as FastAPI, Pydantic V2, SQLAlchemy 2.0, and PostgreSQL. The project is ready to run with Docker and comes with migration files for easy setup.

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **Pydantic V2**: A Python data validation library.
- **SQLAlchemy 2.0**: An ORM for mapping Python objects to database tables.
- **PostgreSQL**: A relational database for storing data.
- **Redis**: In-memory data structure store, used for caching.
- **Uvicorn**: ASGI server for serving the FastAPI application.

## 1. Models Included

The project includes the following models:
- **Product**: Represents products with attributes like `id`, `name`, `price`, etc.
- **Category**: Represents categories that can contain products.
- **Review**: Represents reviews for products with attributes such as `title`, `body`, `status`.
- **User**: Represents user accounts for authentication purposes (login and signup supported).

## 2. API Endpoints

The project supports the following CRUD operations for each entity:

- **Product**:
  - Create, Read, Update, and Delete operations.
- **Category**:
  - Create, Read, Update, and Delete operations.
- **Review**:
  - Create, Read, Update, and Delete operations.
- **User**:
  - User login, signup, and user management.

## 3. Prerequisites

Ensure you have the following installed before starting:

- **Docker** and **Docker Compose**
- **Python 3.9+** (if running manually)
- **Poetry** (if running manually)

### Environment Variables

Make sure you have a `.env` file inside the `src` folder with the following variables configured:

```env
# Database configuration
POSTGRES_USER="your_postgres_user"
POSTGRES_PASSWORD="your_password"
POSTGRES_SERVER="your_server"
POSTGRES_PORT=5432
POSTGRES_DB="your_db"

# Redis configuration
REDIS_CACHE_HOST="localhost"
REDIS_CACHE_PORT=6379
```

## 4. Running the Project with Docker

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd python-task
   ```

2. Start the services with Docker Compose:
   ```sh
   docker compose up
   ```

3. Access the FastAPI Swagger documentation at [http://localhost:8000/docs](http://localhost:8000/docs) to explore and test the APIs.

## 5. Running Manually (Without Docker)

1. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

2. Start the PostgreSQL and Redis containers if you haven't already:
   ```sh
   docker run -d -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=1234 postgres
   docker run -d -p 6379:6379 --name redis redis:alpine
   ```

3. Run the FastAPI application:
   ```sh
   poetry run uvicorn src.app.main:app --reload
   ```

## 6. Database Migrations

### Running Migrations
Migration files are already pushed to the repository, so you can run the following command to apply them:

1. Ensure you are inside the `src` folder:
   ```sh
   cd src
   ```

2. Run the migrations:
   ```sh
   poetry run alembic upgrade head
   ```

## 7. Proof of API Functionality

The API functionality includes CRUD operations for Product, Category, and Review, as well as user authentication. Below are example screenshots showing the creation of each entity:

- **Product Creation**
- **Category Creation**
- **Review Creation**

(Screenshots to be added here later)

## 8. Testing the API

- You can test the API endpoints using the Swagger UI available at [http://localhost:8000/docs](http://localhost:8000/docs).

## 9. License

This project is licensed under the MIT License.

## 10. Contact

For any inquiries, please reach out to the project owner.
```