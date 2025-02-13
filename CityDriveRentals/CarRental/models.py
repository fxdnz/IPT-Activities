from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    loyalty_points = models.FloatField(default=0.00)
    country = models.CharField(max_length=100, default='Philippines')
    language = models.CharField(max_length=100, default='English')

    def get_full_name(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        return f"{first_name} {last_name}"

    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        db_table = 'customer'

    
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50, choices=[('sedan', 'Sedan'), ('suv', 'SUV'), ('luxury', 'Luxury')])
    transmission = models.CharField(max_length=50, choices=[('automatic', 'Automatic'), ('manual', 'Manual')])
    fuel_type = models.CharField(max_length=50, choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'),('electric', 'Electric')])
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    gps = models.BooleanField(default=False)
    child_seats = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vehicle_type} {self.transmission} {self.fuel_type}"
    
    class Meta:
        db_table = 'vehicle'


class Booking(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    payment_type = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('digital_wallet', 'Digital Wallet')])
    payment_status = models.BooleanField(default=False)
    booking_status = models.CharField(max_length=50, choices=[('successful', 'Successful'), ('failed', 'Failed')])

    def get_full_name(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        return f"{first_name} {last_name}"

    def __str__(self):
        return f"Booking by {self.get_full_name()} at {self.pickup_location} {self.pickup_date} {self.booking_status}"
    
    class Meta:
        db_table = 'booking'
        ordering = ['payment_status', 'pickup_date']
        unique_together = ['user', 'vehicle', 'pickup_date']
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"



class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')])

    def __str__(self):
        return f"Review for {self.vehicle.vehicle_type}: {self.rating}"
    
    class Meta:
        db_table = 'review'
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['rating']