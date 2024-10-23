from django.http import Http404
from realty.models import Flat, Floor, Entrance, Building, Project


class FlatRepository:
    def get_all_flats(self):
        return Flat.objects.select_related("floor")

    def get_flat_by_id(self, flat_id):
        try:
            return Flat.objects.get(pk=flat_id)
        except Flat.DoesNotExist:
            raise Http404("Квартира с таким id не найдена.")

    def get_flats_by_floor(self, floor_id):
        return Flat.objects.filter(floor_id=floor_id)

    def get_flats_by_entrance(self, entrance_id):
        return Flat.objects.filter(floor__entrance_id=entrance_id)

    def get_flats_by_building(self, building_id):
        return Flat.objects.filter(floor__entrance__building_id=building_id)

    def get_flats_by_project(self, project_id):
        return Flat.objects.filter(
            floor__entrance__building__project_id=project_id
        )


class FloorRepository:
    def get_all_floors(self):
        return Floor.objects.select_related("entrance")

    def get_floor_by_id(self, floor_id):
        try:
            return Floor.objects.get(pk=floor_id)
        except Floor.DoesNotExist:
            raise Http404("Этаж с таким id не найден.")

    def get_floors_by_entrance(self, entrance_id):
        return Floor.objects.filter(entrance_id=entrance_id)

    def get_floors_by_building(self, building_id):
        return Floor.objects.filter(entrance__building_id=building_id)


class EntranceRepository:
    def get_entrances_by_building(self, building_id):
        return Entrance.objects.filter(building_id=building_id)


class BuildingRepository:
    def get_buildings_by_project(self, project_id):
        return Building.objects.filter(project_id=project_id)
