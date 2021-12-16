from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from booking.models import ReservedPlace
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import BookingSerializersCRUD


class BookingViewSet(viewsets.ModelViewSet):
    queryset = ReservedPlace.objects.all()
    serializer_class = BookingSerializersCRUD
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        if self.action in ['list', 'create', 'retrieve']:
            return self.queryset.filter(user=self.request.user)
        return self.queryset.all()

    def get_permissions(self):
        if self.action in ['list', 'create', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def booking_all(self, request):
        queryset = ReservedPlace.objects.all()
        serializer = BookingSerializersCRUD(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
