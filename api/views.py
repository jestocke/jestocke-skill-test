from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers.booking_param_serializer import BookingParamSerializer
from api.serializers.booking_serializer import BookingSerializer
from booking.models import Booking


class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer  # I'm used to serpy to serialize data from database

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = BookingParamSerializer(data=request.query_params)
        if serializer.is_valid() is False:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        storage_box = request.query_params.get("storage_box", None)
        order = request.query_params.get("order_by", None)
        if storage_box is not None:
            qs = qs.filter(storage_box=storage_box)
        if order is not None:
            qs = qs.order_by(order)

        data = BookingSerializer(qs, many=True).data
        return Response(data={'error': False, 'message': None, 'results': data})
