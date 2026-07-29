from django.db import models


class Subject(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class ClassRoom(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Class Room"
        verbose_name_plural = "Class Rooms"

    def __str__(self):
        return self.name


from django.conf import settings


class StudyRoom(models.Model):

    ROOM_TYPES = (
        ("public", "Public"),
        ("private", "Private"),
    )

    name = models.CharField(
        max_length=200,
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="study_rooms",
    )

    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name="study_rooms",
    )

    description = models.TextField(
        blank=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_rooms",
    )

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="joined_rooms",
        blank=True,
    )

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES,
        default="public",
    )

    room_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    max_members = models.PositiveIntegerField(
        default=30,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name