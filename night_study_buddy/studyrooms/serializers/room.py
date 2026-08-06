from rest_framework import serializers

from studyrooms.models import StudyRoom


class StudyRoomSerializer(serializers.ModelSerializer):

    subject = serializers.CharField(source="subject.name")
    classroom = serializers.CharField(source="classroom.name")
    created_by = serializers.CharField(source="created_by.username")
    members_count = serializers.SerializerMethodField()

    class Meta:
        model = StudyRoom

        fields = (
            "id",
            "name",
            "subject",
            "classroom",
            "description",
            "created_by",
            "room_type",
            "max_members",
            "members_count",
            "created_at",
        )

    def get_members_count(self, obj):
        return obj.members.count()