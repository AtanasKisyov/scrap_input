from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Production(models.Model):

    PRODUCTION_NAME_MAX_LENGTH = 15
    PRODUCTION_NAME_MIN_LENGTH = 2

    production_name = models.CharField(
        max_length=PRODUCTION_NAME_MAX_LENGTH,
        validators=(
            MaxLengthValidator(PRODUCTION_NAME_MAX_LENGTH),
            MinLengthValidator(PRODUCTION_NAME_MIN_LENGTH),
        )
    )

    def __str__(self):
        return f'{self.production_name}'


class Area(models.Model):

    AREA_NAME_MAX_LENGTH = 15
    AREA_NAME_MIN_LENGTH = 2

    area_name = models.CharField(
        max_length=AREA_NAME_MAX_LENGTH,
        validators=(
            MaxLengthValidator(AREA_NAME_MAX_LENGTH),
            MinLengthValidator(AREA_NAME_MIN_LENGTH),
        )
    )

    production = models.ForeignKey(
        Production,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.area_name}'


class Material(models.Model):

    MATERIAL_NUMBER_MAX_LENGTH = 30
    MATERIAL_NUMBER_MIN_LENGTH = 5
    MATERIAL_DESCRIPTION_MAX_LENGTH = 50
    MATERIAL_DESCRIPTION_MIN_LENGTH = 2

    material_number = models.CharField(
        max_length=MATERIAL_NUMBER_MAX_LENGTH,
        validators=(
            MaxLengthValidator(MATERIAL_NUMBER_MAX_LENGTH),
            MinLengthValidator(MATERIAL_NUMBER_MIN_LENGTH),
        )
    )

    material_description = models.CharField(
        max_length=MATERIAL_DESCRIPTION_MAX_LENGTH,
        validators=(
            MaxLengthValidator(MATERIAL_DESCRIPTION_MAX_LENGTH),
            MinLengthValidator(MATERIAL_DESCRIPTION_MIN_LENGTH),
        )
    )

    material_price = models.FloatField()

    material_weight = models.FloatField()


class ScrapTable(models.Model):

    material_number = models.CharField(
        max_length=Material.MATERIAL_NUMBER_MAX_LENGTH,
        validators=(
            MaxLengthValidator(Material.MATERIAL_NUMBER_MAX_LENGTH),
            MinLengthValidator(Material.MATERIAL_NUMBER_MIN_LENGTH),
        )
    )

    material_description = models.CharField(
        max_length=Material.MATERIAL_DESCRIPTION_MAX_LENGTH,
        validators=(
            MaxLengthValidator(Material.MATERIAL_DESCRIPTION_MAX_LENGTH),
            MinLengthValidator(Material.MATERIAL_DESCRIPTION_MIN_LENGTH),
        )
    )

    scrap_quantity = models.IntegerField()

    scrap_price = models.FloatField()

    scrap_weight = models.FloatField()

    scrapper = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
