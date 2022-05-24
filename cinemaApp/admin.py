from django.contrib import admin

# Register your models here.
from cinemaApp.models import Seance, Hall, Movie, Genre, Place, Booking, Profile

admin.site.register(Seance)
admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Place)
admin.site.register(Booking)
admin.site.register(Profile)

