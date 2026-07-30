from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from studyrooms.serializers import CreateStudyRoomSerializer
from studyrooms.services.study_room_service import StudyRoomService


class CreateStudyRoomView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):

        if request.user.role not in ["teacher", "admin"]:
            return Response(
                {
                    "message":
                    "Only teachers and admins can create study rooms."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = CreateStudyRoomSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        StudyRoomService.create_room(
            serializer.validated_data,
            request.user
        )

        return Response(
            {
                "message":
                "Study room created successfully."
            },
            status=status.HTTP_201_CREATED,
        )