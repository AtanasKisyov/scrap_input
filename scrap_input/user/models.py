from django.contrib.auth import get_user_model
from django.db import models


AuthUser = get_user_model()


class Profile(models.Model):

    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    STAFF = 'Staff'
    CONTROLLER = 'Controller'
    SCRAPPER = 'Scrapper'

    USER_ROLES = (
        (STAFF, STAFF),
        (CONTROLLER, CONTROLLER),
        (SCRAPPER, SCRAPPER),
    )

    employee_id = models.IntegerField()

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
    )

    user_role = models.CharField(
        max_length=max([len(choice) for choice, _ in USER_ROLES]),
        choices=USER_ROLES,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
