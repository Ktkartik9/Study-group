from rest_framework import serializers
from accounts.models import User


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "phone",
            "class_name",
            "parent_email",
        ]

        read_only_fields = [
            "id",
            "role",
        ]