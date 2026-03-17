from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(str(user), 'clark@dc.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Avengers', description='Avengers Team')
        user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, date='2024-01-01')
        self.assertIn('tony@marvel.com', str(activity))

    def test_workout_creation(self):
        team = Team.objects.create(name='X-Men', description='X-Men Team')
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Cardio')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Justice League', description='Justice League Team')
        user = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertIn('bruce@dc.com', str(leaderboard))
