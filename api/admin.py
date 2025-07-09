from django.contrib import admin
from .models import MuscleGroup, WorkoutPlan, Exercise

admin.site.register(MuscleGroup)
admin.site.register(WorkoutPlan)
admin.site.register(Exercise)
