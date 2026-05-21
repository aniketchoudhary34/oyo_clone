from django.urls import path
from .views import BookingListView,MyBookingsView

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('my-bookings/', MyBookingsView.as_view(), name='my-bookings'),
]