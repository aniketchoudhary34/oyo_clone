from django.db import models

from users.models import CustomUser
from hotels.models import Hotel, Room
import uuid

class Booking(models.Model):
    status_choices = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        )
    payment_choices =(
        ('online', 'Online'),
        ('offline', 'Pay at Hotel'),
    )
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name='bookings')  
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    payment_status = models.CharField(max_length=20, choices=payment_choices, default='offline')
    created_at = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField(max_length=20, unique=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):        # ← auto generate unique booking ID
        if not self.booking_id:
            self.booking_id = str(uuid.uuid4())[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.username} - {self.room}"