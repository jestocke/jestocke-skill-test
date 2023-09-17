from datetime import date

import pytest

from booking.models import Booking


@pytest.mark.django_db
class TestBookingAdminSort:

    def setUp(self, client, admin_user):
        self.admin_booking_url = '/admin/booking/booking/'

        client.force_login(admin_user)
        Booking.objects.create(created_on=date(2023, 9, 1), tenant=1, start_date=date(2023, 9, 1),
                               end_date=date(2023, 3, 1), storage_box=3)
        Booking.objects.create(created_on=date(2021, 2, 5), tenant=2, start_date=date(2021, 2, 5),
                               end_date=date(2021, 12, 1), storage_box=2)
        Booking.objects.create(created_on=date(2022, 8, 11), tenant=3, start_date=date(2022, 8, 11),
                               end_date=date(2022, 12, 1), storage_box=3)

    def test_bookings_are_displayed(self, client, admin_user):
        """Ensure booking list is displayed on the view"""
        self.setUp(client, admin_user)
        response = client.get(self.admin_booking_url)
        content = str(response.content)

        assert response.status_code == 200

        assert f'<a href="{self.admin_booking_url}1/change/">1</a>' in content
        assert f'<a href="{self.admin_booking_url}2/change/">2</a>' in content
        assert f'<a href="{self.admin_booking_url}3/change/">3</a>' in content

    def test_bookings_are_sorted_by_created_date(self, client, admin_user):
        """Ensure booking list is in descending order"""
        self.setUp(client, admin_user)
        response = client.get(self.admin_booking_url)

        displayed_bookings = response.context['cl'].result_list
        booking_tenant = [booking.tenant for booking in displayed_bookings]

        expected_order = [3, 2, 1]
        assert booking_tenant == expected_order

    def test_booking_can_be_filtered_by_surface(self, client, admin_user):
        """Ensure booking can be filtered by surface"""
        self.setUp(client, admin_user)
        response = client.get(self.admin_booking_url)
        assert 'By storage box' in str(response.content)

        filter_url = f'{self.admin_booking_url}?storage_box=2'
        filter_response = client.get(filter_url)

        assert f'{self.admin_booking_url}2/change/' in str(filter_response.content)
        assert f'{self.admin_booking_url}1/change/' not in str(filter_response.content)
        assert f'{self.admin_booking_url}3/change/' not in str(filter_response.content)

    def test_booking_can_be_filtered_by_availability(self, client, admin_user):
        """Ensure we can filter booking with a date range"""
        self.setUp(client, admin_user)
        response = client.get(self.admin_booking_url)
        assert 'Start date' in str(response.content)
        assert 'End date' in str(response.content)

        filter_url = f'{self.admin_booking_url}?start_date__gte=2021-01-1&end_date__lte=2022-12-31'
        filtered_response = client.get(filter_url)

        assert f'{self.admin_booking_url}3/change/' in str(filtered_response.content)
        assert f'{self.admin_booking_url}2/change/' in str(filtered_response.content)
        assert f'{self.admin_booking_url}1/change/' not in str(
            filtered_response.content
        )
