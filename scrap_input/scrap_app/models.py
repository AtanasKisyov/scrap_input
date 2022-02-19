from django.db import models


class Material(models.Model):

    material_number = models.CharField(max_length=10)

    inserted_on = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class ActiveMaterial(Material):

    material_description = models.CharField(
        max_length=30
    )

    weight = models.FloatField(
        null=True,
        blank=True,
    )


class ScrapTable(Material):
    CHOICES = (
        ('Twisting Area', 'Twisting Area'),
        ('Ultra Sonic Welding Area', 'Ultra Sonic Welding Area'),
        ('Manual Crimping Area', 'Manual Crimping Area'),
        ('Tube Area', 'Tube Area'),
    )
    user = models.CharField(
        max_length=20,
    )

    area = models.CharField(
        max_length=max([len(x) for (_, x) in CHOICES]),
        choices=CHOICES
    )

    quantity = models.IntegerField()
