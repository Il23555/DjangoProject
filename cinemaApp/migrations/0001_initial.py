# Generated by Django 3.1.3 on 2021-11-25 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('row_count', models.IntegerField()),
                ('place_count', models.IntegerField()),
            ],
            options={
                'db_table': 'hall',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('director', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('row', models.IntegerField()),
                ('place', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'place',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'seance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cinemaApp.place')),
                ('seance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cinemaApp.seance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
