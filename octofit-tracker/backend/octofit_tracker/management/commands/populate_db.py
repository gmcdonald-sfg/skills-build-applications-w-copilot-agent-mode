
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Workout, Activity, Leaderboard
from django.db import connection
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Delete all data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Superman', email='superman@dc.com', team=dc),
        ]
        User.objects.bulk_create(users)

        # Refresh users from DB to get PKs
        users = list(User.objects.all())

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do as many pushups as you can.'),
            Workout(name='Running', description='Run for 30 minutes.'),
            Workout(name='Cycling', description='Cycle for 10 miles.'),
        ]
        Workout.objects.bulk_create(workouts)
        workouts = list(Workout.objects.all())

        # Create activities (assign random workouts to users)
        activities = []
        today = date.today()
        for i, user in enumerate(users):
            for j, workout in enumerate(workouts):
                activities.append(Activity(
                    user=user,
                    workout=workout,
                    date=today - timedelta(days=(i+j)),
                    duration_minutes=30 + 5*j,
                    points=10*(j+1)
                ))
        Activity.objects.bulk_create(activities)

        # Calculate leaderboard (sum points per team)
        team_points = {team.id: 0 for team in Team.objects.all()}
        for activity in Activity.objects.all():
            team_points[activity.user.team.id] += activity.points
        for team in Team.objects.all():
            Leaderboard.objects.create(team=team, total_points=team_points[team.id])

        # Ensure unique index on email (MongoDB)
        with connection.cursor() as cursor:
            cursor.execute('''db.get_collection('octofit_tracker_user').createIndex({"email": 1}, {"unique": true})''')

        self.stdout.write(self.style.SUCCESS('Database population complete.'))
