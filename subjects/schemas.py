from typing import Optional, List

from pydantic import BaseModel

from users.schemas import StudentProfileSchema


class SubjectSchema(BaseModel):
    professor_id: int
    name: str
    theory: int
    practice: str
    credits: int
    ects: int

    class Config:
        orm_mode = True


class SubjectPartialUpdateSchema(BaseModel):
    subject_id: Optional[int] = None
    student_id: Optional[int] = None
    mid_grade: Optional[int] = None
    mid_average: Optional[int] = None
    fin_grade: Optional[int] = None
    fin_average: Optional[int] = None
    total: Optional[int] = None


class RegisterSubjectSchema(BaseModel):
    subject_id: int
    student_id: int

    class Config:
        orm_mode = True


class RegisteredStudentsSchema(BaseModel):
    subject_id: int
    students: List[StudentProfileSchema] = []


