from fastapi import HTTPException, status
from fastapi_sqlalchemy import db

from subjects.models import Subject, RegisterSubject
from subjects.schemas import SubjectSchema, RegisterSubjectSchema, SubjectPartialUpdateSchema


def create_subject(request: SubjectSchema):
    new_subject = Subject(professor_id=request.professor_id,
                          name=request.name,
                          theory=request.theory,
                          practice=request.practice,
                          credits=request.credits,
                          ects=request.ects,
                          mid_grade=request.mid_grade,
                          fin_grade=request.fin_grade,
                          total=request.total)
    db.session.add(new_subject)
    db.session.commit()
    db.session.refresh(new_subject)
    return new_subject


def register_subject(request: RegisterSubjectSchema):
    new_subject = RegisterSubject(subject_id=request.subject_id)
    db.session.add(new_subject)
    db.session.commit()
    db.session.refresh(new_subject)
    return new_subject


def all_subjects():
    subjects = db.session.query(Subject).all()
    return subjects


def update_subject(id: int, request: SubjectPartialUpdateSchema):
    subject = db.session.query(RegisterSubject).filter(RegisterSubject.id == id).first()
    if not subject:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Subject with id {id} not found")

    subject.mid_average = (subject.mid_grade * 40) / 100
    subject.fin_average = (subject.fin_grade * 60) / 100
    subject.total = subject.mid_average + subject.fin_average

    data = request.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(subject, key, value)

    db.session.add(subject)
    db.session.commit()
    db.session.refresh(subject)

    return "Success"


def registered_students():
    subjects = db.session.query(RegisterSubject).filter(RegisterSubject.student).first()
    return subjects


def subject_detail(id: int):
    subject = db.session.query(Subject).filter(Subject.id == id).first()
    if not subject:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Subject with the id {id} is not available")
    return subject


def registered_subject_detail(id: int):
    subject = db.session.query(RegisterSubject).filter(RegisterSubject.id == id).first()
    if not subject:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"id {id} is not available")
    return subject

