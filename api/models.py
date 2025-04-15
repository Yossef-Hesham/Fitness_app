from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Profile(models.Model):
    
    class Sport_type(models.TextChoices):
        Trademill = 'Trademill'
        stairmaster = 'stairmaster'
        boxing = 'boxing'
        swimming = 'swimming'
        

    user = models.OneToOneField(User,default=False, unique=True, on_delete=models.CASCADE)
    DateOfbirth = models.DateField(blank=True, null=True)
    Age = models.FloatField(max_length=4, null=True)
    picture = models.ImageField(null=True)
    Is_coach = models.BooleanField()
    Weight = models.FloatField(null=True)
    Height = models.FloatField(null=True)
    Cardio_type = models.CharField(max_length=12,choices=Sport_type.choices)
    
    def __str__(self):
        return self.user.username

class WorkoutDay(models.Model):
    class SportType(models.TextChoices):
        CHEST = 'Push', 'Chest'
        BACK = 'Back', 'Back'
        ARM = 'Arm', 'Arm'
        LEG = 'Leg', 'Leg'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.CharField(max_length=6, choices=SportType.choices)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.workout} - {self.date.strftime('%Y-%m-%d')}"


class Exercise(models.Model):
    Workout = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE, related_name='exercises', null=True)
    name = models.CharField(max_length=20, null=True, blank=False)
    weight = models.IntegerField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    persent_failure = models.PositiveSmallIntegerField(validators=[MinValueValidator(2), MaxValueValidator(10)], default=8)
    def __str__(self):
        return self.name