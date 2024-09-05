# User Service

The **User Service Project** is a Django-based microservice that provides CRUD operations for user management. It supports pagination, sorting, JWT-based authentication, and role-based access control (RBAC).

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Migrations](#database-migrations)
- [Deployment](#deployment)
- [Switching Between Environments](#switching-between-environments)

## Features

- **CRUD Operations**: Create, Read, Update, and Delete users.
- **Pagination and Sorting**: Easily paginate user lists and sort by username or creation date.
- **JWT Authentication**: Secure API endpoints with JWT tokens.
- **Role-Based Access Control**: Differentiate access based on user roles (e.g., Admin, User).
- **Docker Support**: Includes `Dockerfile` and `docker-compose` for easy deployment.
- **Custom Base Model with Soft Deleting**: This project includes a custom base model that implements soft deleting functionality. Rather than permanently deleting records from the database, soft deleting marks them as deleted without removing them, allowing for easier data recovery or auditing.
  - A `deleted_at` field is added to models to indicate if a record is soft deleted.
  - Soft-deleted records excluded from queries by default, but you can explicitly include them for recovery purposes.
- **Custom User Model**: Includes a custom user model implementation for flexibility.
- **Deployment Mode**: Designed to support deployment modes, including **development (local)** and **production**. Each mode has its own set of configurations, including settings, requirements, Dockerfiles, and Docker Compose files. This setup allows for easy switching between different environments.
- **API Documentation**: The project includes Swagger integration for easy-to-navigate, interactive API documentation. Developers can view and interact with the API endpoints directly through the Swagger UI.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.10+** installed on your machine.
- **Virtualenv** or another method for managing virtual environments.
- **Docker** and **Docker Compose**.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Fsnk2001/user-service.git
cd user-service
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

- For development:
    ```bash
    pip install -r requirements.txt
    ```

- For production:
    ```bash
    pip install -r requirements-production.txt
    ```

## Environment Variables

Create a `.env` file in the project root directory and add the required environment.
You can copy the `.env.example` file:

```bash
cp .env.example .env
```

To generate a unique `SECRET_KEY` and set it in your `.env` file, use the provided script.

```bash
python generate_secret_key.py
```

This script will:

- Copy the `.env.example` file to `.env` if `.env` does not already exist.
- Generate a unique `SECRET_KEY` and add it to the `.env` file, ensuring you have a secure key for your application.

## Database Migrations

Apply the migrations to set up your database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Deployment

To deploy the project using Docker Compose, run this:

- For development:
    ```bash
    docker compose up --build -d
    ```

- For production:
    ```bash
    docker compose -f docker-compose-production.yml up --build -d
    ```

## Switching Between Environments

To switch between development and production settings, modify the environment variable `DJANGO_SETTINGS_MODULE` when
running the application.

- For development:
    ```bash
    export DJANGO_SETTINGS_MODULE=user_service.settings.local
    ```

- For production:
    ```bash
    export DJANGO_SETTINGS_MODULE=user_service.settings.production
    ```
