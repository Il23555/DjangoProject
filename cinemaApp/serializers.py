from rest_framework import serializers
from cinemaApp.models import Seance, Genre, Movie, Booking, Hall, Place, Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=6, max_length=100, write_only=True)

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    image = serializers.ImageField(allow_null=True, use_url=True)

    class Meta:
            model = Profile
            fields = ('id', 'user', 'image')
            read_only_fields = ('id', 'user',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'director', 'country', 'duration', 'year')


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ('id', 'name', 'row_count', 'place_count')


class SeanceSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Seance
        fields = ('id', 'hall', 'movie', 'date', 'time')


class PlaceSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)

    class Meta:
        model = Place
        fields = ('id', 'hall', 'row', 'place', 'status')


class BookingSerializer(serializers.ModelSerializer):
    seance = SeanceSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'seance', 'place', 'user')


class BookingSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'seance', 'place', 'user')
