from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Court(models.Model):
    court_number = models.IntegerField(unique=True)
    court_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Court {self.court_number}"

class Availability(models.Model):
    court = models.ForeignKey('Court', on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Availability for {self.court} on day {self.day_of_week}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    duration = models.IntegerField()  # In minutes
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Booking for {self.user} on {self.court} at {self.booking_time}"