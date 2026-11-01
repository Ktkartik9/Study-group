from django.urls import path
from studyrooms.views import CreateStudyRoomView , StudyRoomListView , StudyRoomDetailView , StudyRoomUpdateView , StudyRoomDeleteView 
from studyrooms.views import JoinStudyRoomView
from studyrooms.views import LeaveStudyRoomView


urlpatterns = [

    path("create/",CreateStudyRoomView.as_view(),name="create-study-room",),
    path("",StudyRoomListView.as_view(),name="study-room-list",),
    path("<int:pk>/",StudyRoomDetailView.as_view(),name="study-room-detail",), 
    path("<int:pk>/update/",StudyRoomUpdateView.as_view(),name="study-room-update",),
    path(
    "<int:pk>/delete/",
    StudyRoomDeleteView.as_view(),
    name="study-room-delete",),
    path(
    "<int:pk>/delete/",
    StudyRoomDeleteView.as_view(),
    name="study-room-delete",),
    path(
    "<int:pk>/join/",
    JoinStudyRoomView.as_view(),
    name="study-room-join",
    ),
    path(
    "<int:pk>/leave/",
    LeaveStudyRoomView.as_view(),
    name="study-room-leave",
),
]

