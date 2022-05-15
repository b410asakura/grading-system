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
def update_subject(id: int, request: SubjectPartialUpdateSchema):
    return crud.update_subject(id, request)


@router.get("/")
def all_subjects():
    return crud.all_subjects()


@router.get("/registered_students")
def registered_students_per_subject(current_user: User = Depends(get_current_user)):
    return crud.registered_students()


@router.get("/dww")
def all_subdwdjects():
    return crud.statistic()



# @router.get("/{id}", status_code=200, response_model=UserResponse)
# def user_detail(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not found")
#     return user