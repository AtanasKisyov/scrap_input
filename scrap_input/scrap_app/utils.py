from scrap_input.scrap_app.models import CompareScrapTable


def update_user_scrap_weight(user_id, material, quantity):

    try:

        current_user = CompareScrapTable.objects.get(user_id=user_id)

    except CompareScrapTable.DoesNotExist:

        current_user = CompareScrapTable(
            user_id=user_id,
        )

    registered_weight = material.material_weight * quantity
    current_user.registered_weight += registered_weight
    current_user.save()
