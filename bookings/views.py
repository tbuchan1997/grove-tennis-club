from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Court, Booking, Availability
from datetime import datetime, time, timedelta, date

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, 'bookings/signup.html', {'form': form})

def book_slot(request):
    courts = Court.objects.all().order_by('court_number')
    date_str = request.GET.get('date')
    if date_str:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            date_obj = localdate()
    else:
        date_obj = localdate()

    start_hour = 8
    end_hour = 22
    time_slots = [(time(h, 0), time(h + 1, 0)) for h in range(start_hour, end_hour)]

    # Change availability_data to a dictionary keyed by court number
    availability_data = {}
    for court in courts:
        court_availability = []
        for start, end in time_slots:
            availability = Availability.objects.filter(
                court=court, date=date_obj, start_time=start
            ).first()
            court_availability.append({'start': start, 'availability': availability})
        availability_data[court.court_number] = court_availability

    context = {
        'courts': courts,
        'time_slots': time_slots,
        'availability_data': availability_data,  # Now a dictionary
        'selected_date': date_obj,
    }
    return render(request, 'bookings/book_slot.html', context)

def make_booking(request, court_id):
    court = Court.objects.get(id=court_id)
    
    # Handle booking logic: check if the user has already made a booking at the chosen time
    booking_time = request.POST['booking_time']
    if Booking.objects.filter(court=court, booking_time=booking_time, is_active=True).exists():
        messages.error(request, "This slot is already booked.")
        return redirect('book_slot')

    # Create the booking
    duration = int(request.POST['duration'])
    booking = Booking.objects.create(
        user=request.user,
        court=court,
        booking_time=booking_time,
        duration=duration,
        is_active=True
    )
    
    messages.success(request, f"Booking confirmed for Court {court.court_number} at {booking_time}.")
    return redirect('book_slot')
