from django.db import models


class Material(models.Model):

    material_number = models.CharField(max_length=10)

    inserted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ActiveMaterial(Material):

    material_description = models.CharField(
        max_length=30
    )


class ScrapTable(Material):

    quantity = models.IntegerField()
