from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from studyrooms.models import StudyRoom
from studyrooms.serializers import StudyRoomSerializer , StudyRoomDetailSerializer
from rest_framework.generics import RetrieveAPIView


class StudyRoomListView(ListAPIView):

    serializer_class = StudyRoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            StudyRoom.objects
            .filter(is_active=True)
            .select_related(
                "subject",
                "classroom",
                "created_by",
            )
            .prefetch_related("members")
            .order_by("-created_at")
        )

class StudyRoomDetailView(RetrieveAPIView):

    serializer_class = StudyRoomDetailSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    queryset = (
        StudyRoom.objects
        .select_related(
            "subject",
            "classroom",
            "created_by",
        )
        .prefetch_related("members")
    )