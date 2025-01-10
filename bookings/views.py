from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Court, Booking

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
    today_day_of_week = datetime.now().weekday() #Get todays day of the week 
    bookings = Booking.objects.filter(is_active=True)  # Fetch active bookings
    return render(request, 'bookings/book_slot.html', {'courts': courts, 'bookings': bookings})
    # Dictionary to hold court availability for today
    availability_for_today = {}
    for court in courts:
        # Get the availability for the court for today
        available_slots = Availability.objects.filter(court=court, day_of_week=today_day_of_week)
        availability_for_today[court] = available_slots

        # Pass the courts and their availability to book_slot.html
    return render(request, 'book_slot.html', {
        'courts': courts,
        'availability_for_today': availability_for_today
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
