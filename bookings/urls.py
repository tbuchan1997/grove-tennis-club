from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('book_slot/', views.book_slot, name='book_slot'),
    path('booking_form/<int:availability_id>/', views.show_booking_form, name='booking_form'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('make_booking/', views.make_booking, name='make_booking'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('reschedule_booking/', views.reschedule_booking, name='reschedule_booking'),
]
