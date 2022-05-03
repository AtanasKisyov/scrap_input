from django.db import models


class Production(models.Model):

    PRODUCTION_NAME_MAX_LENGTH = 15

    production_name = models.CharField(
        max_length=PRODUCTION_NAME_MAX_LENGTH,
    )

    def __str__(self):
        return f'{self.production_name}'


class Area(models.Model):

    AREA_NAME_MAX_LENGTH = 15

    area_name = models.CharField(
        max_length=AREA_NAME_MAX_LENGTH,
    )

    production = models.ForeignKey(
        Production,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.area_name}'


class Material(models.Model):

    MATERIAL_NUMBER_MAX_LENGTH = 30
    MATERIAL_DESCRIPTION_MAX_LENGTH = 50

    material_number = models.CharField(
        max_length=MATERIAL_NUMBER_MAX_LENGTH,
    )

    material_description = models.CharField(
        max_length=MATERIAL_DESCRIPTION_MAX_LENGTH,
    )

    material_price = models.FloatField()

    material_weight = models.FloatField()


class ScrapTable(models.Model):

    material_number = models.CharField(
        max_length=Material.MATERIAL_NUMBER_MAX_LENGTH,
    )

    material_description = models.CharField(
        max_length=Material.MATERIAL_DESCRIPTION_MAX_LENGTH,
    )

    scrap_quantity = models.IntegerField()

    scrap_price = models.FloatField()

    scrap_weight = models.FloatField()
