# Bookpluck API
[![codecov][codecov-image]][codecov-url]
[![Quality Gate Status][sonar-image]][sonar-url]

## About the Project


Bookpluck API is a Library Management System developed purely for educational purposes. This RESTful API, built with Flask and SQLAlchemy, simulates the operations of a library, including managing books, authors, users, and loans.

> **Important Note**: This application is not intended for real-world use and is designed solely as a learning tool for developers who want to build RESTful APIs using Python and Flask.

## Key Features

- Virtual management of books and authors
- Simulated user control (members, librarians, administrators)
- Loan and return simulation system
- Sample report generation
- RESTful API documentation for study purposes

## Tech Stack

- Python 3.12
- Flask
- SQLAlchemy
- PostgreSQL
- JWT for authentication
- Docker and Docker Compose
- Alembic for database migrations

## Requirements

- Python 3.12 or higher
- Docker and Docker Compose
- Git

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/pedrodalvy/bookpluck-api.git
   cd bookpluck-api
   ```

2. Build and start the Docker containers:
   ```
   docker compose up --watch
   ```

3. The API will be accessible at `http://localhost:5000`.

## Running Tests

To run the tests, use the following command:

```
poetry run pytest
```

## Educational Purpose

The Bookpluck API is designed to provide hands-on experience in building RESTful APIs. Users are encouraged to explore the code, experiment with changes, and use the project as a base for their own learning and experimentation.

[codecov-image]: https://codecov.io/gh/pedrodalvy/bookpluck-api/graph/badge.svg?token=YI9cQLmJQb
[codecov-url]: https://codecov.io/gh/pedrodalvy/bookpluck-api
[sonar-image]: https://sonarcloud.io/api/project_badges/measure?project=pedrodalvy_bookpluck-api&metric=alert_status
[sonar-url]: https://sonarcloud.io/summary/new_code?id=pedrodalvy_bookpluck-api
