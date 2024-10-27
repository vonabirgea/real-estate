from django.http import Http404
from .repositories import FlatRepository
from .models import Building, Entrance, Flat


def get_all_objects(model):
    return model.objects.all()


def get_object_by_pk(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404


class FlatsSelector:
    repository = FlatRepository()

    def get_all(self) -> tuple[int, list[FlatRepository.FlatData]]:
        flats = FlatsSelector.repository.get_all()
        num_of_flats = len(flats)
        return num_of_flats, flats

    def get_one(self, flat_id: int) -> FlatRepository.FlatData | None:
        flat = FlatsSelector.repository.get_by_id(flat_id)
        return flat

    def get_by_floor(
        self, floor_id: int
    ) -> tuple[int, list[FlatRepository.FlatData]]:
        flats = FlatsSelector.repository.get_by_floor(floor_id)
        flats_on_floor = len(flats)
        return flats_on_floor, flats


def count_entities(queryset):
    return queryset.count()


def get_flats_by_building(building_id):
    return Flat.objects.select_related("floor__entrance__building").filter(
        floor__entrance__building_id=building_id
    )


def count_flats_in_building(building_id):
    entrances = Entrance.objects.select_related("building").filter(
        building_id=building_id
    )
    total_flats_in_building = 0
    for entrance in entrances:
        total_flats_in_building += entrance.flats_count
    return total_flats_in_building


def get_buildings_by_project(project_id):
    buildings = Building.objects.select_related("project").filter(
        project_id=project_id
    )
    return buildings


def count_flats_in_project(project_id):
    entrances = Entrance.objects.select_related("building__project").filter(
        building__project_id=project_id
    )
    total_flats = 0
    for entrance in entrances:
        total_flats += entrance.flats_count
    return total_flats
