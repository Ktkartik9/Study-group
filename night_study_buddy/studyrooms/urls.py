from django.urls import path

from studyrooms.views import CreateStudyRoomView

urlpatterns = [

    path("create/",CreateStudyRoomView.as_view(),name="create-study-room",),

]