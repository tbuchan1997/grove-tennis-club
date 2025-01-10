from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Court(models.Model):
    court_number = models.IntegerField(unique=True)
    court_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Court {self.court_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    duration = models.IntegerField()  # In minutes
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Booking for {self.user} on {self.court} at {self.booking_time}"