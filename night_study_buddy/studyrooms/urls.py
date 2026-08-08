from django.urls import path

from studyrooms.views import CreateStudyRoomView , StudyRoomListView , StudyRoomDetailView , StudyRoomUpdateView



urlpatterns = [

    path("create/",CreateStudyRoomView.as_view(),name="create-study-room",),
    path("",StudyRoomListView.as_view(),name="study-room-list",),
    path("<int:pk>/",StudyRoomDetailView.as_view(),name="study-room-detail",), 
    path("<int:pk>/update/",StudyRoomUpdateView.as_view(),name="study-room-update",),
    
]

