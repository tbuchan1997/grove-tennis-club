from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('book_slot/', views.book_slot, name='book_slot'),
    path('booking_form/<int:availability_id>/', views.show_booking_form, name='booking_form'),
    path('make_booking/', views.make_booking, name='make_booking'),
]
