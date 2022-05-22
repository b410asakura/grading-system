from fastapi import APIRouter, Depends

from deps.oauth2 import get_current_user
from subjects import crud
from subjects.schemas import SubjectSchema, RegisterSubjectSchema, SubjectPartialUpdateSchema
from users.models import User

router = APIRouter(
    prefix="/subject",
    tags=["subjects"]
)


@router.post("/", response_model=SubjectSchema)
def create_subject(request: SubjectSchema):
    return crud.create_subject(request)


@router.post("/register", response_model=RegisterSubjectSchema)
def register_subject(request: RegisterSubjectSchema,
                     current_user: User = Depends(get_current_user)):
    return crud.register_subject(request)


@router.patch('/{id}')
def update_registered_subject(id: int, request: SubjectPartialUpdateSchema):
    return crud.update_subject(id, request)


@router.get("/")
def all_subjects():
    return crud.all_subjects()


@router.get("/registered_students")
def registered_students_per_subject(current_user: User = Depends(get_current_user)):
    return crud.registered_students()


@router.get("/subject_detail/{id}", status_code=200)
def subject_detail(id: int):
    return crud.subject_detail(id)


@router.get("/{id}", status_code=200)
def registered_subject_detail(id: int):
    return crud.registered_subject_detail(id)