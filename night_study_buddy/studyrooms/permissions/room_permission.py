from rest_framework.permissions import BasePermission


class IsTeacherOrAdmin(BasePermission):
    
    message = "Only teachers and admins can perform this action."

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role in ["teacher", "admin"]
        )

class IsRoomOwnerOrAdmin(BasePermission):
    
    message = "Only the room creator or admin can perform this action."

    def has_object_permission(self, request, view, obj):

        return (
            request.user.is_authenticated
            and (
                obj.created_by == request.user
                or request.user.role == "admin"
            )
        )