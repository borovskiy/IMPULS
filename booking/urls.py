from django.urls import path
from .views import ListParkingSpace, CreatingBooking, DeleteBooking, UpdateBooking

urlpatterns = [
    path('', ListParkingSpace.as_view(), name='list_booking'),
    path('add_booking/', CreatingBooking.as_view(), name='add_booking'),
    path('<int:pk>/', UpdateBooking.as_view(), name='update_booking'),
    path('<int:pk>/delete/', DeleteBooking.as_view(), name='delete_booking'),
]
