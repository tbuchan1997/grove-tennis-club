# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from bookings.models import Availability, Court
from datetime import datetime, time, timedelta
from unittest import mock

class AvailabilityModelTest(TestCase):

    @mock.patch('datetime.date.today', return_value=datetime(2025, 1, 13).date())  # Mocking the method
    def test_default_availability(self, mock_today):
        court = Court.objects.create(court_number=1, court_type="Hard")
        # Create an availability instance without setting 'is_available'
        availability = Availability.objects.create(
            court_id=1,  
            date=mock_today(),  # Use the mocked date here
            start_time="10:00",
            end_time="11:00",
        )
        
        # Check if 'is_available' is set to True by default
        self.assertTrue(availability.is_available)

    @mock.patch('datetime.date.today', return_value=datetime(2025, 1, 13).date())  # Mocking the method
    def test_create_default_availability(self, mock_today):
        # Mock today's date
        today = mock_today()

        # Create test courts
        for i in range(1, 5):
            Court.objects.create(court_number=i, court_type="Standard")

        # Call the method to create default availability
        Availability.create_default_availability()

        # Get today's date and time slots
        start_time = time(8, 0)
        end_time = time(22, 0)
        total_slots = 14  # 8am to 10pm in 1-hour slots

        # Check that slots are created for each court
        for court in Court.objects.all():
            slots = Availability.objects.filter(court=court, date=today)
            self.assertEqual(slots.count(), total_slots)

            # Verify slot times
            current_time = timezone.datetime.combine(today, start_time)
            for slot in slots:
                next_time = current_time + timedelta(minutes=60)
                self.assertEqual(slot.start_time, current_time.time())
                self.assertEqual(slot.end_time, next_time.time())
                self.assertTrue(slot.is_available)
                current_time = next_time

    @mock.patch('datetime.date.today')
    def test_default_availability(self, mock_today):
        # Mock the 'today' method to return a specific date
        mock_today.return_value = datetime(2025, 1, 13).date()  # Example date
        
        court = Court.objects.create(court_number=1, court_type="Hard")
        # Create an availability instance without setting 'is_available'
        availability = Availability.objects.create(
            court_id=1,  
            date=mock_today.return_value,  # Use the mocked date here
            start_time="10:00",
            end_time="11:00",
        )
        
        # Check if 'is_available' is set to True by default
        self.assertTrue(availability.is_available)



class BookSlotViewTest(TestCase):
    @mock.patch('datetime.date.today')
    def setUp(self, mock_today):
        # Mock today's date
        mock_today.return_value = datetime(2025, 1, 13).date()
        
        # Create a court for testing
        self.court = Court.objects.create(court_number=1, court_type="Indoor")
        
        # Create an availability slot for the court
        Availability.objects.create(
            court=self.court,
            date=mock_today.return_value,  # Use the mocked date here
            start_time=datetime.time(10, 0),
            end_time=datetime.time(11, 0),
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

    
    def test_no_duplicate_availability(self):
        # Call the method to create default availability
        Availability.create_default_availability()
        Availability.create_default_availability()

        # Check no duplicate slots are created
        today = timezone.localdate()
        total_slots = Availability.objects.filter(date=today).count()
        self.assertEqual(total_slots, 4 * 14)  # 4 courts * 14 slots
