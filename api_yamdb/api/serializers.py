import datetime as dt

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Categories, Comments, Genres, Reviews, Titles
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255,
        validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            confirmation_code=validated_data['confirmation_code'],
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
        fields = ("username", "email",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )


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


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__'


class TitlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True)
    genre = GenresSerializer(read_only=True, many=True)

    class Meta:
        model = Titles
        fields = '__all__'

    def validate_year(self, value):
        current_year = dt.date.today().year
        if value > current_year:
            raise serializers.ValidationError('Исправьте год')
        return value


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Reviews


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comments
