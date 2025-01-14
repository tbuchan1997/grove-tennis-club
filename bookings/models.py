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
    def create_default_availability(cls, days=7, start_time=time(8, 0), end_time=time(22, 0)):
        """Creates default availability for the next 'days' days."""
        courts = Court.objects.all()
        for day_offset in range(days):
            target_date = timezone.localdate() + timedelta(days=day_offset)
            for court in courts:
                for current_hour in range(start_time.hour, end_time.hour):
                    next_hour = (current_hour + 1) % 24
                    cls.objects.create(
                        court=court,
                        date=target_date,
                        start_time=time(current_hour, 0),
                        end_time=time(next_hour, 0),
                        is_available=True,
                    )

    def is_within_booking_window(self, days=7):
        """Checks if the availability date is within the next 'days' days."""
        return self.date <= timezone.localdate() + timedelta(days=days)

    def __str__(self):
        return f"Availability for {self.court} on {self.date} from {self.start_time} to {self.end_time}"





class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    duration = models.IntegerField()  # In minutes
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Booking for {self.user} on {self.court} at {self.booking_time}"