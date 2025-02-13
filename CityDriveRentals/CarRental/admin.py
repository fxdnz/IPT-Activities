from django.contrib import admin
from .models import Customer, Vehicle, Booking, Review

# Register your models here.

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Review)