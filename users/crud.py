from fastapi import HTTPException, status
from fastapi_sqlalchemy import db

from auth.hashing import Hash
from users.models import StudentProfile, User
from users.schemas import StudentProfileSchema, UserCreateSchema, SuperuserCreateSchema


def create_student_profile(request: StudentProfileSchema):
    new_student = StudentProfile(
        user_id=request.user_id,
        program=request.program,
        advisor=request.advisor
    )
    db.session.add(new_student)
    db.session.commit()
    db.session.refresh(new_student)
    return new_student


def create_users(request: UserCreateSchema):
    new_professor = User(
        first_name=request.first_name,
        last_name=request.last_name,
        staff_id=request.staff_id,
        email=request.email,
        role=request.role,
        photo=request.photo,
        is_superuser=request.is_superuser,
        password=Hash.bcrypt(request.password)
    )

    staff_id = db.session.query(User).filter(User.staff_id == request.staff_id).first()
    if staff_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail= f"an account with {request.s} already exist")

    db.session.add(new_professor)
    db.session.commit()
    db.session.refresh(new_professor)
    return new_professor


def create_superuser(request: SuperuserCreateSchema):
    superuser = User(
        staff_id=request.staff_id,
        password=Hash.bcrypt(request.password)
    )
    superuser.is_superuser = True

    db.session.add(superuser)
    db.session.commit()
    db.session.refresh(superuser)
    return superuser


def is_active(self, user: User) -> bool:
    return user.is_active


def is_superuser(self, user: User) -> bool:
    return user.is_superuser


def all_users():
    users = db.session.query(User).all()
    return users