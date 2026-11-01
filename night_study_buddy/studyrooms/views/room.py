from rest_framework.generics import ListAPIView ,UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from night_study_buddy.studyrooms.permissions.room_permission import IsRoomOwnerOrAdmin
from studyrooms.models import StudyRoom
from studyrooms.serializers import StudyRoomSerializer , StudyRoomDetailSerializer ,UpdateStudyRoomSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView
from studyrooms.permissions import IsStudent




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

class StudyRoomUpdateView(UpdateAPIView):

    serializer_class = UpdateStudyRoomSerializer

    permission_classes = [
        IsAuthenticated,
    
    ]

    queryset = StudyRoom.objects.all()

    def perform_update(self, serializer):

        if not serializer.instance.is_active:
            from rest_framework.exceptions import ValidationError

            raise ValidationError(
                {
                    "message":
                    "Inactive study room cannot be updated."
                }
            )

        serializer.save()

class StudyRoomDeleteView(DestroyAPIView):

    permission_classes = [
        IsAuthenticated,
        IsRoomOwnerOrAdmin,
    ]

    queryset = StudyRoom.objects.all()

    def perform_destroy(self, instance):

        instance.is_active = False
        instance.save(update_fields=["is_active"])




class MyStudyRoomsView(ListAPIView):
    serializer_class = StudyRoomSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def get_queryset(self):
        return (
            StudyRoom.objects
            .filter(
                members=self.request.user,
                is_active=True,
            )
            .select_related(
                "subject",
                "classroom",
                "created_by",
            )
            .order_by("-created_at")
        )