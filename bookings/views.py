from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Court, Booking, Availability
from datetime import datetime, time, timedelta, date
import json  # Import json for pretty printing
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

@login_required
def book_slot(request):
    courts = Court.objects.all().order_by('court_number')
    date_obj = timezone.localdate()
    date_str = request.GET.get('date')
    if date_str:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
            return redirect('book_slot')

    today = timezone.localdate()
    for day_offset in range(7):  # Create availability for the next 7 days
        target_date = today + timedelta(days=day_offset)
        for court in courts:
            if not Availability.objects.filter(court=court, date=target_date).exists():
                start_hour = 8
                end_hour = 22
                for hour in range(start_hour, end_hour):
                    Availability.objects.create(
                        court=court,
                        date=target_date,
                        start_time=time(hour, 0),
                        end_time=time(hour + 1, 0),
                        is_available=True,
                    )

    start_hour = 8
    end_hour = 22
    time_slots = [(time(h, 0), time(h + 1, 0)) for h in range(start_hour, end_hour)]

    availability_data = []
    for court in courts:
        court_availability = []
        for start, end in time_slots:
            try:
                availability = Availability.objects.get(  # Use .get() here
                    court=court, date=date_obj, start_time=start
                )
                if availability.is_within_booking_window():
                    court_availability.append({'start': start, 'availability': availability})
                else:
                    court_availability.append({'start': start, 'availability': None})
            except Availability.DoesNotExist:  # Handle the case where no Availability exists
                court_availability.append({'start': start, 'availability': None})

        availability_data.append({'court': court, 'availability': court_availability})

    context = {
        'courts': courts,
        'time_slots': time_slots,
        'availability_data': availability_data,  # Now a dictionary
        'selected_date': date_obj,
    }
    print(json.dumps(availability_data, indent=4, default=str))  # Print with indentation
    return render(request, 'bookings/book_slot.html', context)

def make_booking(request):
    if request.method == 'POST':
        availability_id = request.POST.get('availability')
        duration = int(request.POST.get('duration', 1))

        try:
            availability = Availability.objects.get(pk=availability_id)
            court = availability.court

            # Handle booking logic: check if the user has already made a booking
            booking_time = availability.start_time  # Use start_time from Availability
            if Booking.objects.filter(court=court, booking_time=booking_time, is_active=True).exists():
                messages.error(request, "This slot is already booked.")
                return redirect('book_slot')

            # Create the booking
            booking = Booking.objects.create(
                user=request.user,
                court=court,
                availability=availability,  # Include availability object here
                booking_date=availability.date,
                booking_time=availability.start_time,
                duration=duration,
                is_active=True,
                booked_by=request.user
            )

            messages.success(request, f"Booking confirmed for Court {court.court_number} at {booking_time}.")
            return redirect('book_slot')

        except Availability.DoesNotExist:
            messages.error(request, 'Selected availability not found.')
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('book_slot') # Redirect to book_slot if not a POST request

def show_booking_form(request, availability_id):
    availability = get_object_or_404(Availability, pk=availability_id)
    court = availability.court
    booking_time = f"{availability.start_time.strftime('%H:%M')} - {availability.end_time.strftime('%H:%M')}"
    return render(request, 'bookings/booking_form.html', {
        'availability': availability,
        'court': court,
        'booking_time': booking_time,
    })