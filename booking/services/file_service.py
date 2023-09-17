import json

from django.db.models import Model


class FileServices:
    @staticmethod
    def import_json_data_in_database(file_path: str, model: Model) -> None:
        """Import data from json file to database"""
        with open(file_path, 'r') as file:
            json_data = json.load(file)

        for item in json_data:
            booking = model(
                tenant=item['fields']['tenant'],
                start_date=item['fields']['start_date'],
                end_date=item['fields']['end_date'],
                storage_box=item['fields']['storage_box'],
            )
            booking.save()
