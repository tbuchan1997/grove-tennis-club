from django.contrib import admin
from .models import Court, Availability, Booking

# Register your models here.
admin.site.register(Court)
admin.site.register(Availability)
admin.site.register(Booking)