from django.urls import path 
from .views import RegisterView,userview,profileview,login_view,dashboard,register_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', userview.as_view(), name='users'),
    path('profile/', profileview.as_view(), name='profile'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register-page/', register_view, name='register-page'),
    path('api/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
]   