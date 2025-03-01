from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Activity(models.Model):
    
    ACTIVITY_CHOICES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('yoga', 'Yoga'),
    ]
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    distance = models.FloatField(help_text="Distance in km", null=True, blank=True)
    calories_burned = models.FloatField(help_text="Calories burned")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return self.activity_type 