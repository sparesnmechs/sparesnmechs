"""Spare parts and speciality model."""
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Common(models.Model):
    """Common fields.
    
    These fields are common to most models hence they are
    defined here to follow the DRY rule
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    description = models.TextField()
    photo = models.ImageField(upload_to="spareparts/")

    def __str__(self):
        """Represent first and last name for human readability."""
        return "{} {}".format(self.first_name, self.last_name)


class CommonFields(models.Model):
    """Common fields.

    These fields are common to most models hence they are
    defined here to follow the DRY rule
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Represent name for human readability."""
        return self.name

    class Meta:
        """Make this class an abstract class."""

        abstract = True


class Store(CommonFields):
    """Create stores.

    Sparedealers have stores. These stores have a name and 
    description defined in class CommonFields
    """


class SpareDealer(Common):
    """Create the spare dealer."""

    store = models.ForeignKey(Store, on_delete=models.PROTECT)


class Mechanic(Common):
    """Create the mechanic."""

    store = models.ForeignKey(Store, on_delete=models.PROTECT)


class CarMake(CommonFields):
    """
    Create a make for a car.

    Car make has a name and description (optional). For example:
    name: Toyota.
    """
    photo = models.ImageField(upload_to="spareparts/car_make")


class CarModel(CommonFields):
    """
    Create a car model.

    Every car make has a car model which has a name and an optional
    description eg. Toyota - Harrier.
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="spareparts/car_model")


class CarOwner(Common):
    """Create a car onwer."""

    car_make = models.ManyToManyField(CarMake)
    car_model = models.ManyToManyField(CarModel)


class SparePartCategory(CommonFields):
    """
    Create the categories for spare parts.

    The sparepart category has a name and description field
    obtianed from class CommonField
    """
    photo = models.ImageField(upload_to="spareparts/category")


class SparePartSubCategory(CommonFields):
    """Spare part subcategory for each category created."""

    category = models.ForeignKey(SparePartCategory, on_delete=models.PROTECT)

    def __str__(self):
        """Represent a spare part subcategory name."""
        return self.name


class Speciality(CommonFields):
    """
    Create fields for mechanic specialities.

    A mechanic has a special area where they are skilled in.
    For example Wiring.
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.PROTECT)

    # def get_absolute_url(self):
    #     """Success URL."""
    #     return reverse('detail', kwargs={'pk': self.pk})


class SparePart(CommonFields):
    """
    Create fields for spare parts.

    Sparedealers deal with selling spareparts to car owners. Eg. Bumper
    """

    CONDITION_CHOICES = [
        ("NEW", "New"),
        ("LOCALLY USED", "Locally Used"),
        ("FOREIGN USED", "Foreign Used"),
    ]

    sparedealer = models.ForeignKey(SpareDealer, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    condition = models.CharField(max_length=255, choices=CONDITION_CHOICES)
    year_of_manufacture = models.CharField(max_length=225)
    category = models.ForeignKey(SparePartCategory, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(
        SparePartSubCategory, on_delete=models.PROTECT
    )
    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="spareparts/")  # Only for development


class FeaturedSparePart(models.Model):
    """Featured AD for a sparepart."""

    sparedealer = models.ForeignKey(SpareDealer, on_delete=models.PROTECT)
    sparepart = models.ManyToManyField(SparePart)
    is_featured = models.BooleanField(default=False)


class FeaturedSpeciality(models.Model):
    """Featured AD for a speciality."""

    mechanic = models.ForeignKey(Mechanic, on_delete=models.PROTECT)
    speciality = models.ManyToManyField(Speciality)
    is_featured = models.BooleanField(default=False) # Half Baked
