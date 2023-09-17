from django.core.management.base import BaseCommand
from booking.models import Booking
from booking.services.file_service import FileServices


class Command(BaseCommand):
    help = 'Import json file in database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Json filepath')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']

        try:
            FileServices.import_json_data_in_database(json_file_path, Booking)

            self.stdout.write(self.style.SUCCESS('Json import succeed'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Json File not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurs: {e}'))
