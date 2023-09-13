from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from market_place.models import Profile, StorageBox


# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid4, editable=False)

    created_on = models.DateTimeField(default=timezone.now, verbose_name=_("Creation date"))

    tenant = models.ForeignKey(
        Profile,
        related_name="booking_set",
        on_delete=models.CASCADE,
        verbose_name=_("Tenant"),
    )

    start_date = models.DateField(verbose_name=_("Start date"))
    end_date = models.DateField(verbose_name=_("End date"))

    storage_box = models.ForeignKey(StorageBox, on_delete=models.CASCADE, verbose_name=_("Related storage box"))
