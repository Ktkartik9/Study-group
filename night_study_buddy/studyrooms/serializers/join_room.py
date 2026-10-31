from rest_framework import serializers


class JoinStudyRoomSerializer(serializers.Serializer):
    room_code = serializers.CharField(
        required=False,
        allow_blank=False,
        write_only=True
    )