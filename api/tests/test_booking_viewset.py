from datetime import date
from django.test import RequestFactory
from rest_framework import status
from django.urls import reverse

from rest_framework.test import APITestCase

from booking.models import Booking


def create_fixtures():
    Booking.objects.create(
        created_on=date(2023, 9, 1),
        tenant=1,
        start_date=date(2023, 9, 1),
        end_date=date(2023, 12, 1),
        storage_box=3,
    )
    Booking.objects.create(
        created_on=date(2021, 2, 5),
        tenant=2,
        start_date=date(2021, 2, 5),
        end_date=date(2021, 12, 1),
        storage_box=2,
    )
    Booking.objects.create(
        created_on=date(2022, 8, 11),
        tenant=3,
        start_date=date(2022, 8, 11),
        end_date=date(2022, 12, 1),
        storage_box=3,
    )


class TestBookingViewset(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('booking-list')

    """
    GET /booking/
    """

    def test_list_booking_with_no_booking_return_200(self):
        """Ensure no error is raised if no booking"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response.data['results'] == []

    def test_list_booking_with_bookings_return_200(self):
        """Ensure bookings are returned if exist"""
        create_fixtures()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert len(response.data['results']) == 3
        assert response.data['results'][0] == {
            'tenant': 1,
            'start_date': '2023-09-01',
            'end_date': '2023-12-01',
            'storage_box': 3
        }
        assert response.data['results'][1] == {
            'tenant': 2,
            'start_date': '2021-02-05',
            'end_date': '2021-12-01',
            'storage_box': 2
        }
        assert response.data['results'][2] == {
            'tenant': 3,
            'start_date': '2022-08-11',
            'end_date': '2022-12-01',
            'storage_box': 3
        }

    def test_list_booking_filtered_by_surface_return_200(self):
        """Ensure we can filter booking list by surface"""
        create_fixtures()

        response = self.client.get(self.url, {'storage_box': 2})
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['tenant'] == 2

    def test_list_filter_filtered_by_surface_with_invalid_value_return_400(self):
        """Ensure it raises an error if an invalid value is passed in query"""
        create_fixtures()

        response = self.client.get(self.url, {'storage_box': "bad_value"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_booking_sorted_by_surface_return_200(self):
        """Ensure we can sort booking by surface"""
        create_fixtures()

        response = self.client.get(self.url, {'order_by': "storage_box"})
        assert len(response.data['results']) == 3
        assert response.data['results'][0]['tenant'] == 2
        assert response.data['results'][1]['tenant'] == 1
        assert response.data['results'][2]['tenant'] == 3

    def test_list_booking_sorted_by_surface_with_invalid_value_return_400(self):
        """Ensure it raises an error if an invalid value is passed in query"""
        create_fixtures()

        response = self.client.get(self.url, {'order_by': "bad_value"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_booking_filtered_and_sorted_return_200(self):
        """Ensure it is possible to sort and filter bookings"""
        create_fixtures()

        response = self.client.get(self.url, {'storage_box': 3, 'order_by': "storage_box"})
        assert len(response.data['results']) == 2
        assert response.data['results'][0]['tenant'] == 1
        assert response.data['results'][1]['tenant'] == 3


