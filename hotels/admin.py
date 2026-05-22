# hotels/admin.py
from django.contrib import admin
from .models import Hotel, Room

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display  = ['name', 'city', 'owner', 'is_approved', 'rating']
    list_filter   = ['city', 'is_approved']
    list_editable = ['is_approved']  # seedha approve karo
    search_fields = ['name', 'city']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room_type', 'price', 'is_available']
    list_filter  = ['room_type', 'is_available']