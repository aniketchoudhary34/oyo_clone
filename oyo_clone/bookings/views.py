from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from hotels.models import Hotel, Room

class BookingListView(APIView):
    def post(self,request):
        if not request.user.is_authenticated:
            return Response({"messages":"login required"},status =status.HTTP_401_UNAUTHORIZED)
        
        if request.user.role != 'customer':
            return Response({"messages": "only customer can book room"},status=status.HTTP_403_FORBIDDEN)
        
        
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            hotel = serializer.validated_data['hotel']
            room = serializer.validated_data['room']
            check_in = serializer.validated_data['check_in']
            check_out = serializer.validated_data['check_out']
            # Check if the room is available for the given dates

            if room.hotel != hotel:
                return Response({"message": "Selected room does not belong to the selected hotel"}, status=status.HTTP_400_BAD_REQUEST) 

            if not room.is_available:
                return Response({"message": "Room is not available for the selected dates"}, status=status.HTTP_400_BAD_REQUEST)
    
            if check_out <= check_in:
                return Response({"message": "Check-out date must be after check-in date"}, status=status.HTTP_400_BAD_REQUEST)
            nights = (check_out - check_in).days
            total_price = nights * room.price
          
            booking = serializer.save(customer=request.user, total_price=total_price)
            return Response({"message": "Room booked successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyBookingsView(APIView):
    def get(self,request):
        if not request.user.is_authenticated:
            return Response({"messages":"login required"},status =status.HTTP_401_UNAUTHORIZED)
        if request.user.role != 'customer':
            return Response({"messages": "only customer can view their bookings"},status=status.HTTP_403_FORBIDDEN)
        bookings = Booking.objects.filter(customer=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)