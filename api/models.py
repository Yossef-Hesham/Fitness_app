from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    
    class Sport_type(models.TextChoices):
        Trademill = 'Trademill'
        stairmaster = 'stairmaster'
        boxing = 'boxing'
        swimming = 'swimming'
        

    user = models.OneToOneField(User,default=False, unique=True, on_delete=models.CASCADE)
    DateOfbirth = models.DateField(blank=True, null=True)
    Age = models.FloatField(max_length=2, null=True)
    picture = models.ImageField(null=True)
    Is_coach = models.BooleanField()
    Weight = models.FloatField(null=True)
    Height = models.FloatField(null=True)
    Cardio_type = models.CharField(max_length=12,choices=Sport_type.choices)
    
    def __str__(self):
        return self.user.username


class Exercise(models.Model):
    
    class Sport_type(models.TextChoices):
        Chest = 'Chest'
        Back = 'Back'
        Arm = 'Arm'
        Leg = 'Leg'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Weight = models.IntegerField()
    num_sets = models.IntegerField()
    num_reps = models.IntegerField()
    persent_failure = models.ValueRange(2, 10)
    Muscle = models.CharField(max_length=6,choices=Sport_type.choices)
    
    def __str__(self):
        return self.Muscle

