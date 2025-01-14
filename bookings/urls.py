from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('book_slot/', views.book_slot, name='book_slot'),
    path('make_booking/<int:court_id>/', views.make_booking, name='make_booking'),
]
