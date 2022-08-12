from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.utils import generate_confirmation_code, send_mail_with_code
from users.models import User
from users.serializers import UserSerializer, TokenSerializer, MeSerializer
from api.permissions import IsSelfOrAdmins

# class AuthCreateUserView(CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = (
#         permissions.AllowAny,
#     )
# 
#     def perform_create(self, serializer):
#         email = self.request.data.get('email')
#         confirmation_code = generate_confirmation_code()
#         serializer.is_valid(raise_exception=True)
#         serializer.save(data=self.request.data, confirmation_code=confirmation_code)
#         send_mail_with_code(email, confirmation_code)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class AuthCreateUserView(APIView):
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request):
        email = self.request.data.get('email')
        confirmation_code = generate_confirmation_code()
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(data=self.request.data, confirmation_code=confirmation_code)
        send_mail_with_code(email, confirmation_code)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class TokenCreateView(APIView):
#     permission_classes = (
#         permissions.AllowAny,
#     )
# 
#     def get_token(self, user):
#         refresh = RefreshToken.for_user(user)
#         return str(refresh.access_token)
# 
#     def post(self, request):
#         user = get_object_or_404(User, username=request.data.get('username'))
#         if user.confirmation_code != request.data.get('confirmation_code'):
#             response = {'confirmation_code': 'Неверный код'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         response = {'token': self.get_token(user)}
#         return Response(response, status=status.HTTP_200_OK)


class TokenCreateView(CreateAPIView):
    permission_classes = (
        permissions.AllowAny,
    )

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=request.data.get('username'))
        if user.confirmation_code != request.data.get('confirmation_code'):
            response = {'confirmation_code': 'Неверный код'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = {'token': self.get_token(user)}
        return Response(response, status=status.HTTP_200_OK)
            
            
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    # permission_classes = (
    #     permissions.IsAuthenticated, 
    #     IsSuperuser | IsAdmin,
    # )
    permission_classes = (IsSelfOrAdmins,)

    @action(
        detail=False,
        permission_classes=(permissions.IsAuthenticated,),    
        methods=['get', 'patch'], 
        url_path='me'
    )
    def get_or_update(self, request):
        user = get_object_or_404(User, username=self.request.user)
        if request.method == 'GET':
            serializer = MeSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = MeSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
