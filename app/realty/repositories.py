from realty.models import Flat, Floor, Entrance, Building, Project


class FlatRepository:
    def get_flats_by_floor(self, floor_id):
        return Flat.objects.filter(floor_id=floor_id)


class FloorRepository:
    def get_floors_by_entrance(self, entrance_id):
        return Floor.objects.filter(entrance_id=entrance_id)


class EntranceRepository:
    def get_entrances_by_building(self, building_id):
        return Entrance.objects.filter(building_id=building_id)


class BuildingRepository:
    def get_buildings_by_project(self, project_id):
        return Building.objects.filter(project_id=project_id)
