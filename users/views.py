from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.role ='customer'
            user.save()
            return Response({"message": "user registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userview(APIView):
    def get (self,request):
        users = CustomUser.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)


class profileview(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response(
            {
                "id": request.user.id,
                "username": request.user.username,
              
                
            }
        )

def login_view(request):
    return render(request, 'users/login.html')

def home_view(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')  
 
def register_view(request):
    return render(request, 'users/register.html')