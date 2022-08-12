from django.conf import settings
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255,
        validators=[UniqueValidator(queryset=User.objects.all())])
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        return user

    def validate_username(self, value):
            if value.lower() == 'me':
                raise serializers.ValidationError(
                    'username "me" not allowed'
                )
            return value

    class Meta:
        model = User
        fields = ( "username", "email", )


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code',)

class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


