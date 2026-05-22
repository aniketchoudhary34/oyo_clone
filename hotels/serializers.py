from rest_framework import serializers
from .models import Hotel,Room



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
      model = Room
      fields = "__all__"

rooms = RoomSerializer(many=True, read_only=True)
#           ↑               ↑         ↑
#     Room ka         many=True =   read_only =
#     serializer      Multiple      Rooms sirf
#     use karo        rooms hain    dekhne ke liye
#                     ek hotel mein Likhne ke liye nahi

class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
      rooms = RoomSerializer(many=True, read_only=True)
      model = Hotel 
      fields = "__all__"
#                ↑
#         Sab fields include karo
#         automatically!

      read_only_fields = [
            'owner',      # Owner khud set hoga
            'rating',     # Rating calculate hogi
            'is_approved' # Admin approve karega
          ]
#       ↑
#       Ye fields user change nahi kar sakta!