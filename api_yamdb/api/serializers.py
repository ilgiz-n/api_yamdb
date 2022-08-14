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
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class TitlesWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    year = serializers.IntegerField()
    genre = serializers.SlugRelatedField(
        queryset=Genres.objects.all(),
        slug_field='slug',
        many=True,
        required=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Categories.objects.all(),
        slug_field='slug',
        many=False,
    )

    class Meta:
        model = Titles
        # fields = ('name', 'year', 'genre', 'category',)
        fields = '__all__'

    def validate_year(self, value):
        current_year = dt.date.today().year
        if value > current_year:
            raise serializers.ValidationError('Исправьте год')
        return value


class TitlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer()
    genre = GenresSerializer(many=True)

    class Meta:
        model = Titles
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )
        read_only_fields = fields


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
