# Hunters Food API

An API that provides all information and data about [Hunters Food App](https://github.com/JoelSoliz/hunters-food-app).

## Table of contents

- [Technologies](#technologies)
- [Setup](#setup)
- [Migrate Database](#migrate-database)

## Technologies

- Python version: 3.10.7
- MySQL version: 8.0.30

## Setup

1. Create a virtual environment before start.

   `python -m venv <name-virtual-environment>`

2. Activate virtual environment.

   `.\<name-virtual-environment>\Scripts\activate` (For Windows)

3. Install project dependencies.

   `pip install -r requirements.txt`

4. Run project.

   `uvicorn main:app --reload`

## Migrate Database

When you modify one of the database models you need to make a migration.

1. Create a revision.

   `alembic revision --autogenerate -m "<description>"`

2. Push updates to database after create a revision.

   `alembic upgrade head`
