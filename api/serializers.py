from rest_framework import serializers
from booking.models import ReservedPlace


class BookingSerializersCRUD(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ReservedPlace
        fields = ('id','user', 'parking_space', 'date_start_parking', 'date_finish_parking',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
