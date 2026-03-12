from django.test import TestCase
from .models import Team, User, Workout, Activity, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='T')
        u = User.objects.create(name='U', email='u@test.com', team=t)
        self.assertEqual(str(u), 'U')
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc')
        self.assertEqual(str(w), 'W')
    def test_activity_create(self):
        t = Team.objects.create(name='T2')
        u = User.objects.create(name='U2', email='u2@test.com', team=t)
        w = Workout.objects.create(name='W2', description='desc2')
        a = Activity.objects.create(user=u, workout=w, date='2024-01-01', duration_minutes=10, points=5)
        self.assertIn('U2', str(a))
    def test_leaderboard_create(self):
        t = Team.objects.create(name='T3')
        l = Leaderboard.objects.create(team=t, total_points=42)
        self.assertIn('T3', str(l))
