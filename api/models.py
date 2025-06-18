from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    height_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    current_weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    
class MuscleGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Exercise(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    muscles = models.ManyToManyField(MuscleGroup, related_name='exercises')
    equipment = models.ManyToManyField(Equipment, related_name='exercises')




class WorkoutPlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='workout_plans')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PlanExercise(models.Model):
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)



class WorkoutLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='workout_logs')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=50, blank=True)
    calories_burned = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)

class WorkoutExerciseLog(models.Model):
    workout = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE, related_name='exercise_logs')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets_completed = models.PositiveIntegerField()
    reps_each = models.PositiveIntegerField()
    weight_used = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)


class WeightLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='weight_logs')
    log_date = models.DateField()
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)

class BodyMeasurement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='measurements')
    log_date = models.DateField()
    chest_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hips_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)



class UserStreak(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='streak')
    current_streak_days = models.PositiveIntegerField(default=0)
    longest_streak_days = models.PositiveIntegerField(default=0)
    last_workout_date = models.DateField(null=True, blank=True)



class WeeklyLeaderboard(models.Model):
    week_start = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='leaderboards')
    workout_count = models.PositiveIntegerField(default=0)
    total_volume = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ('week_start', 'user')





class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50)  # e.g. "WORKOUT_COUNT", "TOTAL_VOLUME"
    target_value = models.PositiveIntegerField()

class UserAchievement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')




