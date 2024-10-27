from dataclasses import dataclass
from datetime import datetime
from django.http import Http404
from realty.models import Flat, Floor, Entrance, Building, Project


class FlatRepository:
    @dataclass
    class FlatData:
        id: int
        number: int
        area: float
        rooms_count: int
        wc_count: int
        floor_id: int
        status: str
        description: str
        created_at: datetime
        last_update: datetime

    def get_all(self):
        flatslist = Flat.objects.select_related("floor")
        list_of_flats = []
        for flat in flatslist:
            flat_data = FlatRepository.FlatData(
                id=flat.id,
                number=flat.number,
                area=flat.area,
                rooms_count=flat.rooms_count,
                wc_count=flat.wc_count,
                floor_id=flat.floor.id,
                status=flat.status,
                description=flat.description,
                created_at=flat.created_at,
                last_update=flat.last_update,
            )
            list_of_flats.append(flat_data)
        return list_of_flats

    def get_by_id(self, flat_id):
        flat = Flat.objects.filter(pk=flat_id)
        if flat:
            flat_data = FlatRepository.FlatData(
                id=flat[0].id,
                number=flat[0].number,
                area=flat[0].area,
                rooms_count=flat[0].rooms_count,
                wc_count=flat[0].wc_count,
                floor_id=flat[0].floor.id,
                status=flat[0].status,
                description=flat[0].description,
                created_at=flat[0].created_at,
                last_update=flat[0].last_update,
            )
            return flat_data
        return None

    def get_by_floor(self, floor_id):
        flatslist = Flat.objects.filter(floor_id=floor_id)
        list_of_flats = []
        for flat in flatslist:
            flat_data = FlatRepository.FlatData(
                id=flat.id,
                number=flat.number,
                area=flat.area,
                rooms_count=flat.rooms_count,
                wc_count=flat.wc_count,
                floor_id=flat.floor.id,
                status=flat.status,
                description=flat.description,
                created_at=flat.created_at,
                last_update=flat.last_update,
            )
            list_of_flats.append(flat_data)
        return list_of_flats

    def get_by_entrance(self, entrance_id):
        return Flat.objects.filter(floor__entrance_id=entrance_id)

    def get_by_building(self, building_id):
        return Flat.objects.filter(floor__entrance__building_id=building_id)

    def get_by_project(self, project_id):
        return Flat.objects.filter(
            floor__entrance__building__project_id=project_id
        )


class FloorRepository:
    @dataclass
    class FloorData:
        id: int
        floor: int
        flats_count: int
        status: str
        description: str
        entrance_id: int

    def get_all(self):
        return Floor.objects.select_related("entrance")

    def get_by_id(self, floor_id):
        try:
            return Floor.objects.get(pk=floor_id)
        except Floor.DoesNotExist:
            raise Http404("Этаж с таким id не найден.")

    def get_by_entrance(self, entrance_id):
        return Floor.objects.filter(entrance_id=entrance_id)

    def get_by_building(self, building_id):
        return Floor.objects.filter(entrance__building_id=building_id)


class EntranceRepository:
    def get_by_building(self, building_id):
        return Entrance.objects.filter(building_id=building_id)


class BuildingRepository:
    def get_by_project(self, project_id):
        return Building.objects.filter(project_id=project_id)
