from .models import Flat, Floor, Entrance, Building, Project

# from realty.repositories import FlatRepository


def get_flats_by_entrance(entrance_id):
    return Flat.objects.select_related("floor__entrance").filter(
        floor__entrance_id=entrance_id
    )
