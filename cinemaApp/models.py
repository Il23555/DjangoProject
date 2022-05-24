from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table = 'profile'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    seance = models.ForeignKey('Seance', models.DO_NOTHING, blank=True, null=True)
    place = models.ForeignKey('Place', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'booking'


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    genre = models.ForeignKey(Genre, models.DO_NOTHING, blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'

    def __str__(self):
        return self.name


class Seance(models.Model):
    id = models.AutoField(primary_key=True)
    hall = models.ForeignKey('Hall', models.DO_NOTHING, blank=True, null=True)
    movie = models.ForeignKey('Movie', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'seance'

    def __str__(self):
        return str(self.movie) + ' ' + str(self.date) + ' ' + str(self.time)


class Hall(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    row_count = models.IntegerField()
    place_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hall'

    def __str__(self):
        return self.name


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    hall = models.ForeignKey(Hall, models.DO_NOTHING, blank=True, null=True)
    row = models.IntegerField()
    place = models.IntegerField()
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'place'

    def __str__(self):
        return str(self.row) + ' ' + str(self.place)



