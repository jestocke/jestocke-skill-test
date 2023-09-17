import pytest

from booking.models import Booking
from booking.services.file_service import FileServices


@pytest.mark.django_db
class TestFileService:
    def test_import_json_data_in_database_with_success(self):
        """Ensure records are created in database"""
        file_path = '../tests/fixtures/sample.json'
        bookings = Booking.objects.all()
        assert bookings.count() == 0
        FileServices.import_json_data_in_database(file_path, Booking)
        bookings = Booking.objects.all()
        assert bookings.count() == 10

    def test_import_json_data_in_database_with_not_valid_parameters_raise_error(self):
        """Ensure we raise an error if json parameters are not valid for the model"""
        file_path = '../tests/fixtures/bad_paramters.json'
        with pytest.raises(KeyError):
            FileServices.import_json_data_in_database(file_path, Booking)
