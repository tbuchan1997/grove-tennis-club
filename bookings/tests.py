# Create your tests here.
from django.test import TestCase
from django.utils import timezone
from .models import Court, Availability, Booking
from django.contrib.auth.models import User
from datetime import time, date, timedelta



class AvailabilityModelTest(TestCase):
    def setUp(self):
        self.court = Court.objects.create(court_number=1, court_type="Hard")

    

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.court = Court.objects.create(court_number=1, court_type="Grass")
        self.availability = Availability.objects.create(
            court=self.court,
            date=date(2024, 1, 2),
            start_time=time(14, 0),
            end_time=time(15, 0),
            is_available=True,
        )

    def test_booking_creation(self):
        booking = Booking.objects.create(
            user=self.user,
            booked_by=self.user,
            court=self.court,
            availability=self.availability,
            booking_date=date(2024, 1, 2),
            booking_time=time(14, 0),
            duration=1,
            is_active=True,
        )
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.booked_by, self.user)
        self.assertEqual(booking.court, self.court)
        self.assertEqual(booking.availability, self.availability)
        self.assertEqual(booking.booking_date, date(2024, 1, 2))
        self.assertEqual(booking.booking_time, time(14, 0))
        self.assertEqual(booking.duration, 1)
        self.assertTrue(booking.is_active)

    def test_booking_cancellation(self):
        booking = Booking.objects.create(
            user=self.user,
            booked_by=self.user,
            court=self.court,
            availability=self.availability,
            booking_date=date(2024, 1, 2),
            booking_time=time(14, 0),
            duration=1,
            is_active=True,
        )
        booking.is_active = False
        booking.save()
        self.assertFalse(booking.is_active)