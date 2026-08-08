from rest_framework import serializers

from studyrooms.models import StudyRoom


class CreateStudyRoomSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyRoom

        fields = (
            "name",
            "subject",
            "classroom",
            "description",
            "room_type",
            "room_code",
            "max_members",
        )

    def validate_max_members(self, value):

        if value < 2:
            raise serializers.ValidationError(
                "Minimum members should be 2."
            )

        if value > 100:
            raise serializers.ValidationError(
                "Maximum members cannot exceed 100."
            )

        return value

    def validate(self, attrs):

        if (
            attrs["room_type"] == "private"
            and not attrs.get("room_code")
        ):
            raise serializers.ValidationError(
                {
                    "room_code":
                    "Room code is required for private rooms."
                }
            )

        return attrs

class UpdateStudyRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyRoom

        fields = (
            "name",
            "subject",
            "classroom",
            "description",
            "room_type",
            "room_code",
            "max_members",
            "is_active",
        )

    def validate_max_members(self, value):

        if value < 2:
            raise serializers.ValidationError(
                "Minimum members should be 2."
            )

        if value > 100:
            raise serializers.ValidationError(
                "Maximum members cannot exceed 100."
            )

        return value

    def validate(self, attrs):

        room_type = attrs.get(
            "room_type",
            self.instance.room_type
        )

        room_code = attrs.get(
            "room_code",
            self.instance.room_code
        )

        if room_type == "private" and not room_code:
            raise serializers.ValidationError(
                {
                    "room_code":
                    "Room code is required for private rooms."
                }
            )

        return attrs