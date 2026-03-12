from rest_framework import viewsets, routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team, User, Workout, Activity, Leaderboard
from .serializers import TeamSerializer, UserSerializer, WorkoutSerializer, ActivitySerializer, LeaderboardSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'teams': '/api/teams/',
        'users': '/api/users/',
        'workouts': '/api/workouts/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
    })

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
