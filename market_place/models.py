from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from djmoney.forms import MoneyField

from market_place.constants import StorageTypes


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(_("First name"), max_length=254)
    last_name = models.CharField(_("Last name"), max_length=254)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name=_('Date of birth')
    )
    # picture = models.ImageField(upload_to="profile_picture")


class StorageBox(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Profile, verbose_name="owner", on_delete=models.CASCADE)

    storage_type = models.CharField(
        _('Type d\'espace'), max_length=32, choices=StorageTypes.choices
    )

    title = models.CharField(verbose_name=_("Ad title"), max_length=512)
    slug = models.SlugField(max_length=128, editable=False, null=True, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True, default="")
    surface = models.IntegerField(_("Surface (m²)"), blank=True, null=True, default=1)
    # monthly_price = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')

    street_number = models.CharField("N°", blank=True, null=True, max_length=128)
    route = models.CharField("route", blank=True, null=True, max_length=512)
    additional_address = models.TextField("additional address", blank=True, null=True)
    postal_code = models.CharField("postal code", max_length=32)
    city = models.CharField("city", max_length=32)

    # image_1 = models.ImageField(upload_to="box_picture")
    # image_2 = models.ImageField(upload_to="box_picture")
    # image_3 = models.ImageField(upload_to="box_picture")
