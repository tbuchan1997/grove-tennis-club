from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Court, Booking
from datetime import datetime

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
    courts = Court.objects.all()  # Fetch all courts

    # Fetch availability slots for today
    today_day_of_week = datetime.datetime.today().weekday()  # 0 - Monday, 6 - Sunday
    availability_for_today = Availability.objects.filter(day_of_week=today_day_of_week)

    return render(request, 'bookings/book_slot.html', {
        'courts': courts,
        'availability': availability_for_today,
    })

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
