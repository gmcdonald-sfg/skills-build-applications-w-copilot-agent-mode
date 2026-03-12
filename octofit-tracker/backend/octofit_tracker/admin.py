from django.contrib import admin
from .models import Team, User, Workout, Activity, Leaderboard

admin.site.register(Team)
admin.site.register(User)
admin.site.register(Workout)
admin.site.register(Activity)
admin.site.register(Leaderboard)
