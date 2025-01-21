from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Court, Booking, Availability
from datetime import datetime, time, timedelta, date
import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.exceptions import ValidationError
import datetime
from dateutil.parser import parse

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

@login_required
def book_slot(request):
    courts = Court.objects.all().order_by('court_number')
    date_obj = timezone.localdate()
    date_str = request.GET.get('date')
    reschedule_id = request.GET.get('reschedule_id')

    if date_str:
        try:
            date_obj = parse(date_str).date()
        except (ValueError, TypeError):  # Handle both ValueError and TypeError
            messages.error(request, "Invalid date format.")
            return redirect('book_slot')

    if reschedule_id:
        try:
            booking_to_cancel = Booking.objects.get(pk=reschedule_id, user=request.user)
            booking_to_cancel.is_active = False
            booking_to_cancel.save()
            messages.success(request, "Your previous booking has been cancelled.")
        except Booking.DoesNotExist:
            messages.error(request, "Booking not found.")
            return redirect('dashboard') # Redirect to dashboard if booking not found

    now = timezone.now()

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
                availability = Availability.objects.get(  
                    court=court, date=date_obj, start_time=start
                )
                if availability.is_within_booking_window():
                    court_availability.append({'start': start, 'availability': availability})
                else:
                    court_availability.append({'start': start, 'availability': None})
            except Availability.DoesNotExist:  # Handle the case where no Availability exists
                court_availability.append({'start': start, 'availability': None})

        availability_data.append({'court': court, 'availability': court_availability})

    for court in courts:
        for availability in Availability.objects.filter(court=court, date=date_obj):
            if availability.date == now.date() and availability.start_time <= now.time():
                availability.is_available = False
                availability.save()

    context = {
        'courts': courts,
        'time_slots': time_slots,
        'availability_data': availability_data,
        'selected_date': date_obj,
    }
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

            availability.is_available = False
            availability.save()
            return render(request, 'bookings/booking_success.html', {'booking': booking})  # Redirect to success page

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

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user, is_active=True).order_by('booking_date', 'booking_time') #Only active bookings
    return render(request, 'bookings/dashboard.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user, is_active=True)
    if request.method == 'POST':
        availability = booking.availability
        booking.is_active = False
        booking.save()
        availability.is_available = True
        availability.save()
        messages.success(request, "Booking cancelled successfully.")
        return redirect('view_bookings')  # Redirect to dashboard
    return render(request, 'bookings/cancel_booking.html', {'booking': booking}) #Render cancel page if not a post request

@login_required
def reschedule_booking(request):
    print("Reschedule view was called!")
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if not booking_id:
            messages.error(request, "Booking ID is missing. Please try again.")
            return redirect('view_bookings')

        try:
            with transaction.atomic():
                booking = get_object_or_404(Booking, pk=booking_id, user=request.user, is_active=True)
                old_availability = booking.availability

                new_date_str = request.POST.get('new_date')
                new_time_str = request.POST.get('new_time')

                try:
                    new_date = datetime.datetime.strptime(new_date_str, '%Y-%m-%d').date()
                    new_time = datetime.datetime.strptime(new_time_str, '%H:%M').time()
                except ValueError as e:
                    messages.error(request, "Invalid date or time format. Please use YYYY-MM-DD and HH:MM.")
                    return redirect('view_bookings')

                old_availability.is_available = True
                old_availability.save()

                try:
                    new_availability = Availability.objects.get(court=booking.court, date=new_date, start_time=new_time, is_available=True)
                except Availability.DoesNotExist:
                    old_availability.is_available = False
                    old_availability.save()
                    messages.error(request, "Selected availability not found.")
                    return redirect('view_bookings')

                if Booking.objects.filter(court=booking.court, booking_time=new_time, booking_date=new_date, is_active=True).exclude(pk=booking.pk).exists():
                    old_availability.is_available = False
                    old_availability.save()
                    messages.error(request, "This slot is already booked.")
                    return redirect('view_bookings')

                booking.booking_date = new_date
                booking.booking_time = new_time
                booking.availability = new_availability
                booking.save()

                new_availability.is_available = False
                new_availability.save()

                messages.success(request, "Booking rescheduled successfully.")
                return redirect('view_bookings')

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
            return redirect('view_bookings')
    return redirect('view_bookings')

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user, booking_date__gte=timezone.now()).order_by('booking_date', 'booking_time')
    courts = Court.objects.all().order_by('court_number')
    today = timezone.localdate()
    start_hour = 8
    end_hour = 22
    time_slots = [(time(h, 0), time(h + 1, 0)) for h in range(start_hour, end_hour)]

    now = timezone.now()  # Get the current time in the appropriate timezone
    bookings = Booking.objects.filter(
        user=request.user,
        booking_date__gte=now.date()  # Only bookings on or after today
    ).exclude(
        booking_date=now.date(), booking_time__lt=now.time()  # Exclude past bookings for today
    ).order_by('booking_date', 'booking_time')

    availability_data = {}
    for court in courts:
        for availability in Availability.objects.filter(court=court, date__gte=today):
            if availability.date == today and availability.start_time <= timezone.now().time():
                continue
            if availability.date not in availability_data:
                availability_data[availability.date] = {}
            if availability.start_time not in availability_data[availability.date]:
                availability_data[availability.date][availability.start_time] = {}
            availability_data[availability.date][availability.start_time][court.id] = availability


    context = {
        'bookings': bookings,  # Existing bookings data, if any
        'courts': courts,
        'time_slots': time_slots,
        'availability_data': availability_data,  # Availability data pre-calculated
        'selected_date': selected_date,  # Date to display
    }

    return render(request, 'bookings/dashboard.html', context)

