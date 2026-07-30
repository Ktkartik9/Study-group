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