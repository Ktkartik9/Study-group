from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from night_study_buddy.studyrooms.models import StudyRoom
from night_study_buddy.studyrooms.serializers.room import StudyRoomDetailSerializer
 
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