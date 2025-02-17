"""

"""

import re
from django.contrib.auth import get_user_model


from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """新規登録"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ユーザーの新しい認証用トークンを作成する"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """認証されたユーザーを管理する"""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """認証されたユーザーを取得する"""
        return self.request.user
