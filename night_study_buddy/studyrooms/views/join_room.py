from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from studyrooms.permissions import IsStudent
from studyrooms.serializers.join_room import JoinStudyRoomSerializer
from studyrooms.services.study_room_service import StudyRoomService


class JoinStudyRoomView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def post(self, request, pk):
        serializer = JoinStudyRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        room = StudyRoomService.join_room(
            room_id=pk,
            user=request.user,
            room_code=serializer.validated_data.get("room_code"),
        )

        return Response(
            {
                "message": "You have joined the study room successfully.",
                "room_id": room.id,
                "room_name": room.name,
            },
            status=status.HTTP_200_OK,
        )