from django.db import models
from django.contrib.auth.models import User
from datetime import time, timedelta, datetime
from django.utils import timezone


# Create your models here.

class Court(models.Model):
    court_number = models.IntegerField(unique=True)
    court_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Court {self.court_number}"

class Availability(models.Model):
    court = models.ForeignKey('Court', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Availability for {self.court} on day {self.date} from {self.start_time} to {self.end_time}"

    @classmethod
    def create_default_availability(cls):
        courts = Court.objects.all()
        today = timezone.localdate() # Todays date, for testing
        start_time = time(8, 0) # Available from 8am
        end_time = time(22, 0) # Until 10pm

        for court in courts:
            current_time = timezone.datetime.combine(today, start_time)

            while current_time.time() < end_time:
                for block in time_blocks:
                    next_time = current_time + timedelta(minutes=60)
                    # Create each slot with start_time, end_time, and availability
                    cls.objects.create(
                        court=court,
                        date=today,
                        start_time=current_time.time(),
                        end_time=next_time.time(),
                    )
                    current_time = next_time





class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    duration = models.IntegerField()  # In minutes
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Booking for {self.user} on {self.court} at {self.booking_time}"