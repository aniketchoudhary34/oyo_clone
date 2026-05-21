from django.urls import path
from .views import Hotellistview

urlpatterns = [
    path('hotels/', Hotellistview.as_view(), name='hotel-list'),

]