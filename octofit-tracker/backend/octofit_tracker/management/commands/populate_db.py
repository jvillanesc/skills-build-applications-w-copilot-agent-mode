from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Eliminar datos existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Crear usuarios
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Crear actividades
        Activity.objects.create(user=tony, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Yoga', duration=20, date=timezone.now().date())

        # Crear workouts
        cardio = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        strength = Workout.objects.create(name='Strength Training', description='Build muscle strength')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(dc)

        # Crear leaderboard
        Leaderboard.objects.create(user=tony, score=120, rank=1)
        Leaderboard.objects.create(user=steve, score=110, rank=2)
        Leaderboard.objects.create(user=bruce, score=105, rank=3)
        Leaderboard.objects.create(user=clark, score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
