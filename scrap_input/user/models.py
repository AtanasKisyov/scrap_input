from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from scrap_input.scrap_app.models import Area, Production

AuthUser = get_user_model()


class UserProfile(models.Model):

    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    STAFF = 'Staff'
    CONTROLLER = 'Controller'
    SCRAPPER = 'Scrapper'

    USER_ROLES = (
        (STAFF, STAFF),
        (CONTROLLER, CONTROLLER),
        (SCRAPPER, SCRAPPER),
    )

    employee_id = models.IntegerField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MaxLengthValidator(FIRST_NAME_MAX_LENGTH),
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MaxLengthValidator(LAST_NAME_MAX_LENGTH),
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        )
    )

    user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
    )

    user_role = models.CharField(
        max_length=max([len(choice) for choice, _ in USER_ROLES]),
        choices=USER_ROLES,
    )

    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        unique=False,
    )

    production = models.ForeignKey(
        Production,
        on_delete=models.CASCADE,
        unique=False,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
