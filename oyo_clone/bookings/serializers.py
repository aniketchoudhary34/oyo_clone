from rest_framework import serializers
from .models import Booking 

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
    
        read_only_fields = [
            'customer',    # Login user se milega
            'total_price', # Calculate hogi
            'booking_id',  # Auto generate hoga
            'status'       # Default pending hoga
        ]
#       ↑
#       User ye fields nahi bhejega
#       System khud set karega!