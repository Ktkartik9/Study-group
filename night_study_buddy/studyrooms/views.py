from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from night_study_buddy.studyrooms.models import StudyRoom
from night_study_buddy.studyrooms.serializers.room import StudyRoomDetailSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from studyrooms.permissions import IsStudent
from studyrooms.services.study_room_service import StudyRoomService
 
class StudyRoomDetailView(RetrieveAPIView):

    serializer_class = StudyRoomDetailSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    queryset = (
        StudyRoom.objects
        .filter(is_active=True)
        .select_related(
            "subject",
            "classroom",
            "created_by",
        )
        .prefetch_related("members")
    )




class LeaveStudyRoomView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def post(self, request, pk):
        room = StudyRoomService.leave_room(
            room_id=pk,
            user=request.user,
        )

        return Response(
            {
                "message": "You have left the study room successfully.",
                "room_id": room.id,
                "room_name": room.name,
            },
            status=status.HTTP_200_OK,
        )