from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('login/',
        LoginView.as_view(template_name='bookings/login.html'),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('book_slot/', views.book_slot, name='book_slot'),
    path('make_booking/<int:court_id>/', views.make_booking, name='make_booking'),
]
