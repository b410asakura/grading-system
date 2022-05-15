from enum import Enum

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Role(Enum):
    PROFESSOR = "professor"
    STUDENT = "student"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    staff_id = Column(String)
    email = Column(String)
    photo = Column(String)
    password = Column(String)
    role = Role = None
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)


class StudentProfile(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref=backref("student", uselist=False))
    program = Column(String)
    advisor = Column(String)
