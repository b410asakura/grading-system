# from fastapi_contrib.permissions import BasePermission
# from starlette.requests import Request
#
# from users.models import User
#
#
# class StudentPermission(BasePermission):
#
#     def has_required_permissions(self, request: Request):
#         return request.user.role.STUDENT
#
#
# class ProfessorPermission(BasePermission):
#
#     def has_required_permissions(self, request: Request):
#         return request.user.role == "Professor"
