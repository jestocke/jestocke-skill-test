from django.utils.translation import gettext_lazy as _


class StorageTypes:
    GARAGE_BOX = "GARAGE_BOX"
    CELLAR = "CELLAR"
    ATTIC = "ATTIC"
    ROOM = "ROOM"
    HANGAR_WAREHOUSE = "HANGAR_WAREHOUSE"
    PARKING = "PARKING"

    choices = (
        (GARAGE_BOX, _("Garage")),
        (CELLAR, _("Cellar")),
        (ATTIC, _("Attic")),
        (ROOM, _("Room")),
        (HANGAR_WAREHOUSE, _("Hangar / Warehouse")),
        (PARKING, _("parking spot")),
    )
