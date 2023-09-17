from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class BookingParamSerializer(serializers.Serializer):
    storage_box = serializers.CharField(required=False)
    order_by = serializers.CharField(required=False)

    valid_filters = ["created_on", "storage_box", "start_date", "end_date"]

    def validate_storage_box(self, value):
        try:
            int(value)
        except ValueError:
            raise ValidationError("Invalid storage box parameter")

    def validate_order_by(self, value):
        if value not in self.valid_filters:
            raise ValidationError("Invalid order parameter")
