from django.conf import settings
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            confirmation_code=validated_data['confirmation_code']
        )
        return user

    class Meta:
        model = User
        fields = ( "username", "email", )

