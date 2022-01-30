from django.db import models


class Material(models.Model):

    material_number = models.CharField(
        max_length=10
    )

    material_description = models.CharField(
        max_length=30
    )


class ScrapTable(models.Model):

    material_number = models.CharField(
        max_length=10
    )

    quantity = models.IntegerField()

    inserted_on = models.DateTimeField(
        auto_now=True
    )
