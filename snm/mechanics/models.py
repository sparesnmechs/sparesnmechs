from django.db import models

from snm.common.models import CommonItemFields, CommonUserFields, Store
from snm.carowners.models import CarMake


class Mechanic(CommonUserFields):
    """Create the mechanic."""

    store = models.ForeignKey(Store, on_delete=models.PROTECT)


class Speciality(CommonItemFields):
    """
    Create fields for mechanic specialities.

    A mechanic has a special area where they are skilled in.
    For example Wiring.
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.PROTECT)
    is_featured = models.BooleanField(default=False)  # Half Baked
