from django.contrib import admin

from .models import Subject, ClassRoom ,StudyRoom



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

@admin.register(StudyRoom)
class StudyRoomAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "subject",
        "classroom",
        "room_type",
        "created_by",
        "max_members",
        "is_active",
    )

    list_filter = (
        "subject",
        "classroom",
        "room_type",
        "is_active",
    )

    search_fields = (
        "name",
    )

    filter_horizontal = (
        "members",
    )