# bookings/tests/test_models.py
from django.test import TestCase
from django.urls import reverse
from bookings.models import Availability, Court
from datetime import datetime

class AvailabilityModelTest(TestCase):

    def test_default_availability(self):
        court = Court.objects.create(court_number=1, court_type="Hard")
        # Create an availability instance without setting 'is_available'
        availability = Availability.objects.create(
            court_id=1,  # Use a valid court ID
            day_of_week=datetime.today().weekday(),  # Use the current day of the week
            start_time="10:00",  # Example start time
            end_time="11:00",  # Example end time
        )
        
        # Check if 'is_available' is set to True by default
        self.assertTrue(availability.is_available)

class BookSlotViewTest(TestCase):

    def setUp(self):
        # Create a court for testing
        self.court = Court.objects.create(court_number=1, court_type="Indoor")
        
        # Create an availability slot for the court
        Availability.objects.create(
            court=self.court,
            day_of_week=datetime.today().weekday(),
            start_time="10:00",
            end_time="11:00",
            is_available=True
        )

    def test_book_slot_view(self):
        # Send a GET request to the 'book_slot' page
        response = self.client.get(reverse('book_slot'))
        
        # Ensure the response is successful (200 OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the availability slots are in the response context
        self.assertIn('availability', response.context)
        self.assertEqual(len(response.context['availability']), 1)  # We created one slot in setUp()
