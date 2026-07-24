from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer


class RefreshTokenSerializer(TokenRefreshSerializer):
    pass