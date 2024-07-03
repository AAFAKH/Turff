from django.db import models
from django.contrib.auth.models import User

class Turf(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='turf_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.user.username} - {self.turf.name} - {self.booking_date} {self.start_time}-{self.end_time}"
