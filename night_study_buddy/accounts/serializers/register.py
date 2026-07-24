from rest_framework import serializers
from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
            "role",
            "phone",
            "class_name",
            "parent_email",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data["role"],
            phone=validated_data.get("phone"),
            class_name=validated_data.get("class_name"),
            parent_email=validated_data.get("parent_email"),
        )

        return user