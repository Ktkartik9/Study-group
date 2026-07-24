from rest_framework_simplejwt.views import TokenRefreshView
from accounts.serializers.refresh import RefreshTokenSerializer


class RefreshTokenView(TokenRefreshView):

    serializer_class = RefreshTokenSerializer