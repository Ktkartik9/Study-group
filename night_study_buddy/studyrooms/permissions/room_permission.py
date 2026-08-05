from rest_framework.permissions import BasePermission


class IsTeacherOrAdmin(BasePermission):
    
    message = "Only teachers and admins can perform this action."

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role in ["teacher", "admin"]
        )

