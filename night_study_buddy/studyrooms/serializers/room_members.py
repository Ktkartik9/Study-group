from rest_framework import serializers


class RoomMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()