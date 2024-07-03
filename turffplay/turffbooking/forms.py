from django import forms
from account.models import Turf, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'start_time', 'end_time']

class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = ['name', 'description', 'address', 'price_per_hour', 'photo']
