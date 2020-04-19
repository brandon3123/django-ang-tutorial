from django.db import models


# Create your models here.
class Book(models.Model):

    # choices=
    # default=
    # unique=
    # blank=
    # null=
    # max-length=
    # EmailField
    title = models.CharField(unique=True,
                             null=False,
                             blank=False,
                             max_length=64)

    #TextField is like  CLOB, CharField is a String
    description = models.TextField(max_length=256,
                                   blank=True)

    # FloatField
    # IntegerField
    # BigIntegerField
    # DecimalField
    price = models.DecimalField(default=0,
                                max_digits=5,
                                decimal_places=2)

    # DateField
    # DateTimeField
    # TimeField
    published = models.DateField(blank=True,
                                 null=True,
                                 default=None)

    is_published = models.BooleanField(default=False)

    # ImageField
    # FileField
    cover = models.ImageField(upload_to="covers/",
                              blank=True)
