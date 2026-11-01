from studyrooms.models import StudyRoom
from django.db import transaction
from rest_framework.exceptions import ValidationError
from studyrooms.models import StudyRoom


class StudyRoomService:

    @staticmethod
    def create_room(validated_data, created_by):

        room = StudyRoom.objects.create(
            created_by=created_by,
            **validated_data
        )

        room.members.add(created_by)

        return room

    @staticmethod
    @transaction.atomic
    def join_room(room_id, user, room_code=None):

        try:
            room = StudyRoom.objects.select_for_update().get(
                id=room_id
            )
        except StudyRoom.DoesNotExist:
            raise ValidationError("Study room not found.")

        if not room.is_active:
            raise ValidationError("This study room is inactive.")

        if room.members.filter(id=user.id).exists():
            raise ValidationError("You have already joined this room.")

        if room.members.count() >= room.max_members:
            raise ValidationError("Study room is full.")

        if room.room_type == "private":
            if not room_code:
                raise ValidationError(
                    {"room_code": "Room code is required."}
                )

            if room.room_code != room_code:
                raise ValidationError(
                    {"room_code": "Invalid room code."}
                )

        room.members.add(user)

        return room

    @staticmethod
    def leave_room(room_id, user):

        try:
            room = StudyRoom.objects.get(id=room_id)
        except StudyRoom.DoesNotExist:
            raise ValidationError("Study room not found.")

        if not room.members.filter(id=user.id).exists():
            raise ValidationError(
                "You are not a member of this study room."
            )

        room.members.remove(user)

        return room