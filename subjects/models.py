from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from users.models import User, StudentProfile

Base = declarative_base()


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True, index=True)
    professor_id = Column(Integer, ForeignKey(User.id))
    professor = relationship(User, backref=backref("subject", uselist=False))
    name = Column(String)
    theory = Column(Integer)
    practice = Column(String)
    credits = Column(Integer)
    ects = Column(Integer)


class RegisterSubject(Base):
    __tablename__ = "register_subject"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey(StudentProfile.id))
    student = relationship(StudentProfile)
    subject_id = Column(Integer, ForeignKey(Subject.id))
    subject = relationship(Subject)
    mid_grade = Column(Integer)
    mid_average = Column(Integer)
    fin_grade = Column(Integer)
    fin_average = Column(Integer)
    total = Column(Integer)







