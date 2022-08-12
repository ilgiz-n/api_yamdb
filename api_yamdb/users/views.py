from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from users.utils import generate_confirmation_code, send_mail_with_code
from users.models import User
from users.serializers import UserSerializer


class AuthCreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def perform_create(self, serializer):
        email = self.request.data.get('email')
        confirmation_code = generate_confirmation_code()
        serializer.is_valid(raise_exception=True)
        serializer.save(data=self.request.data, confirmation_code=confirmation_code)
        send_mail_with_code(email, confirmation_code)
        return Response({
            'status': 200,
            'data': serializer.data
        })


class TokenCreateView(APIView):
    permission_classes = (
        permissions.AllowAny,
    )

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request):
        user = get_object_or_404(User, username=request.data.get('username'))
        if user.confirmation_code != request.data.get('confirmation_code'):
            response = {'confirmation_code': 'Неверный код'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = {'token': self.get_token(user)}
        return Response(response, status=status.HTTP_200_OK)
