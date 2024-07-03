from django.shortcuts import render
from django.views.generic import ListView,TemplateView
# Create your views here.

class CustomerHomeView(TemplateView):
    template_name="custhome.html"

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import Turf, Booking
from .forms import BookingForm, TurfForm

def turf_list(request):
    turfs = Turf.objects.all()
    return render(request, 'list.html', {'turfs': turfs})

@login_required
def book_turf(request, turf_id):
    turf = Turf.objects.get(id=turf_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.turf = turf
            booking.total_price = (booking.end_time - booking.start_time).seconds / 3600 * turf.price_per_hour
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'bookturf.html', {'turf': turf, 'form': form})

# @login_required
# def booking_success(request):
#     return render(request, 'turfbooking/booking_success.html')

# @login_required
# def my_bookings(request):
#     bookings = Booking.objects.filter(user=request.user)
#     return render(request, 'turfbooking/my_bookings.html', {'bookings': bookings})

# @login_required
# def add_turf(request):
#     if request.method == 'POST':
#         form = TurfForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('turf_list')
#     else:
#         form = TurfForm()
    
#     return render(request, 'turfbooking/add_turf.html', {'form': form})

