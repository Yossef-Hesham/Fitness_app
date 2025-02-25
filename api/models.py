from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    class SportType(models.TextChoices):
        TREADMILL = 'Trademill', 'Treadmill'
        STAIRMASTER = 'stairmaster', 'Stairmaster'
        BOXING = 'boxing', 'Boxing'
        SWIMMING = 'swimming', 'Swimming'

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.FloatField(null=True)
    # picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_coach = models.BooleanField(default=False)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    cardio_type = models.CharField(max_length=20, choices=SportType.choices)

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

