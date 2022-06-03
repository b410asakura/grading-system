# GRADING SYSTEM API

---
# Built With

> ### `Fast API` - The framework used
> ### `PostgreSQL` - The database used
> ### `Poetry` - For dependency management
> ### `Alembic` - For database migrations
> ### `Swagger` - Documentation. Built in Fast API


# Team members:

1) Aiana Abdyrakhmanova (backend)
2) Zebiniso Sultonmurodova ([frontend repository](https://github.com/santiill/grade_system))

# Deployed to Heroku

### [Heroku](https://grading-alatoo.herokuapp.com/docs)

---
# Getting started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
# Prerequisites
This is a project written using Python, Fast API

1. Clone the repository
```
https://github.com/luianqi/grading-system.git
```
2. Initialize Poetry and install poetry.lock
```
Poetry install 
```
3. Install the requirements
```
pip install -r requirements.txt
```
4. Create a new PostgreSQL database

In your terminal:
```
psql postgres
CREATE DATABASE databasename
\c databasename
```
5. Run the server
```
python -m uvicorn main:app --reload
```

