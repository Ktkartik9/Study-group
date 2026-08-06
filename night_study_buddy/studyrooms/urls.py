from django.urls import path

from studyrooms.views import CreateStudyRoomView , StudyRoomListView

urlpatterns = [

    path("create/",CreateStudyRoomView.as_view(),name="create-study-room",),
    path("",StudyRoomListView.as_view(),name="study-room-list",),

]

