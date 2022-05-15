from fastapi import APIRouter

from users import crud
from users.schemas import StudentProfileSchema

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/create_student_profile")
def student_profile(request: StudentProfileSchema):
    return crud.create_student_profile(request)


@router.get("/")
def all_users():
    return crud.all_users()
