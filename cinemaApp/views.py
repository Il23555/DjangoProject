from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from cinemaApp.models import Seance, Movie, Genre, Place, Booking, Hall, Profile
from cinemaApp.serializers import SeanceSerializer, MovieSerializer, GenreSerializer, PlaceSerializer, \
    BookingSerializer, HallSerializer, UserSerializer, ProfileSerializer, BookingSerializer1


class ProfileView(APIView):

    def get(self, request, format=None):
        user = User.objects.get(username=request.user)
        user_profile = Profile.objects.get(user=user)
        data = {'user': {'username': user.username},
                'image': user_profile.image or None}

        serializer = ProfileSerializer(user_profile, data=data, context={"request": request})

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        user = User.objects.get(username=request.user)
        user_profile = Profile.objects.get(user=user)
        data = {'user': {'username': user.username},
                'image': request.data.get('image')}

        serializer = ProfileSerializer(user_profile, data=data, context={"request": request})

        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data:
                serializer.save(user=user)

        return Response(serializer.data)


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeanceViewList(APIView):
    def get(self, request):
        sessions = Seance.objects.all()
        sessions_serializer = SeanceSerializer(instance=sessions, many=True)
        return Response(sessions_serializer.data)

    def post(self, request):
        serializer = SeanceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class SeanceView(APIView):
    def get(self, request, pk):
        try:
            seance = Seance.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        seance_serializer = SeanceSerializer(instance=seance)
        return Response(seance_serializer.data)

    def put(self, request, pk):
        try:
            seance = Seance.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        seance_serializer = SeanceSerializer(instance=seance, data=request.data, partial=True)
        if seance_serializer.is_valid():
            seance_serializer.save()
        return Response(seance_serializer.data)

    def delete(self, request, pk):
        try:
            seance = Seance.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        seance_serializer = SeanceSerializer(instance=seance)
        seance.delete()
        return Response(seance_serializer.data)


class MovieViewList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(instance=movies, many=True)
        return Response(movies_serializer.data)

    def post(self, request):
        movie_serializer = MovieSerializer(data=request.data)
        if movie_serializer.is_valid(raise_exception=True):
            movie_serializer.save()
        return Response(movie_serializer.data)


class MovieView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie_serializer = MovieSerializer(instance=movie)
        return Response(movie_serializer.data)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie_serializer = MovieSerializer(instance=movie, data=request.data, partial=True)
        if movie_serializer.is_valid():
            movie_serializer.save()
        return Response(movie_serializer.data)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie_serializer = MovieSerializer(instance=movie)
        movie.delete()
        return Response(movie_serializer.data)


class GenreViewList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        genres_serializer = GenreSerializer(instance=genres, many=True)
        return Response(genres_serializer.data)

    def post(self, request):
        genre_serializer = GenreSerializer(data=request.data)
        if genre_serializer.is_valid(raise_exception=True):
            genre_serializer.save()
        return Response(genre_serializer.data)


class GenreView(APIView):
    def get(self, request, pk):
        try:
            genre = Genre.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre_serializer = GenreSerializer(instance=genre)
        return Response(genre_serializer.data)

    def put(self, request, pk):
        try:
            genre = Genre.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre_serializer = GenreSerializer(instance=genre, data=request.data, partial=True)
        if genre_serializer.is_valid():
            genre_serializer.save()
        return Response(genre_serializer.data)

    def delete(self, request, pk):
        try:
            genre = Genre.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre_serializer = GenreSerializer(instance=genre)
        genre.delete()
        return Response(genre_serializer.data)


class PlaceViewList(APIView):
    def get(self, request):
        places = Place.objects.all()
        places_serializer = PlaceSerializer(instance=places, many=True)
        return Response(places_serializer.data)

    def post(self, request):
        place_serializer = PlaceSerializer(data=request.data)
        if place_serializer.is_valid(raise_exception=True):
            place_serializer.save()
        return Response(place_serializer.data)


class PlaceView(APIView):
    def get(self, request, pk):
        try:
            place = Place.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        place_serializer = PlaceSerializer(instance=place)
        return Response(place_serializer.data)

    def put(self, request, pk):
        try:
            place = Place.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        place_serializer = PlaceSerializer(instance=place, data=request.data, partial=True)
        if place_serializer.is_valid():
            place_serializer.save()
        return Response(place_serializer.data)

    def delete(self, request, pk):
        try:
            place = Place.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        place_serializer = PlaceSerializer(instance=place)
        place.delete()
        return Response(place_serializer.data)


class BookingViewList(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        if request.query_params.get('user'):
            user_id = request.query_params.get('user')
            bookings = bookings.filter(user=user_id)
        bookings_serializer = BookingSerializer(instance=bookings, many=True)
        return Response(bookings_serializer.data)

    def post(self, request):
        booking_serializer = BookingSerializer1(data=request.data)
        if booking_serializer.is_valid(raise_exception=True):
            booking_serializer.save()
        return Response(booking_serializer.data)


class BookingView(APIView):
    def get(self, request, pk):
        try:
            booking = Booking.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        booking_serializer = BookingSerializer(instance=booking)
        return Response(booking_serializer.data)

    def put(self, request, pk):
        try:
            booking = Booking.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        booking_serializer = BookingSerializer(instance=booking, data=request.data, partial=True)
        if booking_serializer.is_valid():
            booking_serializer.save()
        return Response(booking_serializer.data)

    def delete(self, request, pk):
        try:
            booking = Booking.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        booking_serializer = BookingSerializer(instance=booking)
        booking.delete()
        return Response(booking_serializer.data)


class HallViewList(APIView):
    def get(self, request):
        halls = Hall.objects.all()
        halls_serializer = HallSerializer(instance=halls, many=True)
        return Response(halls_serializer.data)

    def post(self, request):
        hall_serializer = HallSerializer(data=request.data)
        if hall_serializer.is_valid(raise_exception=True):
            hall_serializer.save()
        return Response(hall_serializer.data)


class HallView(APIView):
    def get(self, request, pk):
        try:
            hall = Hall.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        hall_serializer = HallSerializer(instance=hall)
        return Response(hall_serializer.data)

    def put(self, request, pk):
        try:
            hall = Hall.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        hall_serializer = HallSerializer(instance=hall, data=request.data, partial=True)
        if hall_serializer.is_valid():
            hall_serializer.save()
        return Response(hall_serializer.data)

    def delete(self, request, pk):
        try:
            hall = Hall.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        hall_serializer = HallSerializer(instance=hall)
        hall.delete()
        return Response(hall_serializer.data)
