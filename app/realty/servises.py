from .models import Flat, Floor, Entrance, Building, Project

from .repositories import FlatRepository, FloorRepository


def list_flats():
    repository = FlatRepository()
    flats = repository.get_all_flats()
    total_flats = flats.count()
    return total_flats, flats


def list_flats_on_floor(floor_id):
    repository = FlatRepository()
    flats = repository.get_flats_by_floor(floor_id)
    total_flats = flats.count()
    return total_flats, flats


def get_flat(flat_id):
    repository = FlatRepository()
    flat = repository.get_flat_by_id(flat_id)
    return flat


def list_floors():
    repository = FloorRepository()
    floors = repository.get_all_floors()
    total_floors = floors.count()
    return total_floors, floors


def get_floor(floor_id):
    floor_repository = FloorRepository()
    flat_repository = FlatRepository()
    floor = floor_repository.get_floor_by_id(floor_id)
    flats = flat_repository.get_flats_by_floor(floor_id)
    flats_list = []
    for flat in flats:
        flats_list.append(flat.id)

    return floor, flats_list
