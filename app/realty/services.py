from .models import Flat, Floor, Entrance, Building, Project

from .repositories import FlatRepository, FloorRepository


def list_floors():
    repository = FloorRepository()
    floors = repository.get_all()
    total_floors = floors.count()
    return total_floors, floors


def get_floor(floor_id):
    floor_repository = FloorRepository()
    flat_repository = FlatRepository()
    floor = floor_repository.get_floor_by_id(floor_id)
    flats = flat_repository.get_by_floor(floor_id)
    flats_list = []
    for flat in flats:
        flats_list.append(flat.id)

    return floor, flats_list
