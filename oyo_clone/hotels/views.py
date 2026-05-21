from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Hotel
from .serializers import HotelSerializer


class Hotellistview(APIView):
    
    def get(self, request):
        hotels = Hotel.objects.filter(is_approved=True)
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

# Create your views here.
    def post(self,request):
        if not request.user.is_authenticated:
            return Response({"message": "Login required"}, status=status.HTTP_401_UNAUTHORIZED)

        if request.user.role != "owner":
            return Response({"message": "Only hotel owners can add hotels"}, status=status.HTTP_403_FORBIDDEN)

        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({"message":"Hotel added successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)