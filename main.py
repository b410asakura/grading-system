import os

from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi import FastAPI

from auth import auth
from subjects import subject_routes
from users import user_routes

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(auth.router)
app.include_router(user_routes.router)
app.include_router(subject_routes.router)


