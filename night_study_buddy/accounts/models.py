from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('admin', 'Admin'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    class_name = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    parent_email = models.EmailField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.username} - {self.role}"