import os

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi import FastAPI

from auth import auth
from subjects import subject_routes
from users import user_routes

load_dotenv(".env")

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
uri = os.environ["DATABASE_URL"]
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.include_router(auth.router)
app.include_router(user_routes.router)
app.include_router(subject_routes.router)


