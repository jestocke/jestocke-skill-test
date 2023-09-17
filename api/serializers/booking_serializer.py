from rest_framework import serializers

from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'tenant',
            'start_date',
            'end_date',
            'storage_box'
        )