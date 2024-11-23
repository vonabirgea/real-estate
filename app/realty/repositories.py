from realty.models import Flat, Floor, Entrance, Building, Project
from realty.entities import FlatEntity, FloorEntity, EntranceEntity


class FlatRepository:
    def get_all(self) -> list[FlatEntity]:
        all_flats = Flat.objects.select_related("floor")
        list_of_flats = [
            FlatEntity(
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
            for flat in all_flats
        ]
        return list_of_flats

    def get_by_id(self, flat_id: int) -> FlatEntity | None:
        flat = Flat.objects.filter(pk=flat_id).first()
        if flat:
            one_flat = FlatEntity(
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
            return one_flat
        return None

    def get_by_entity(
        self, entity: str, entity_id: int
    ) -> list[FlatEntity] | None:
        query = Flat.objects
        if entity.lower() == "floor":
            flats = query.filter(floor_id=entity_id)
        elif entity.lower() == "entrance":
            flats = query.filter(floor__entrance_id=entity_id)
        elif entity.lower() == "building":
            flats = query.filter(floor__entrance__building_id=entity_id)
        elif entity.lower() == "project":
            flats = query.filter(
                floor__entrance__building__project_id=entity_id
            )
        else:
            return None
        list_of_flats = [
            FlatEntity(
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
            for flat in flats
        ]
        return list_of_flats


class FloorRepository:
    def get_all(self) -> list[FloorEntity]:
        all_floors = Floor.objects.select_related("entrance")
        list_of_floors = [
            FloorEntity(
                id=floor.id,
                storey=floor.storey,
                flats_count=floor.flats_count,
                status=floor.status,
                description=floor.description,
                entrance_id=floor.entrance_id,
                created_at=floor.created_at,
                last_update=floor.last_update,
            )
            for floor in all_floors
        ]
        return list_of_floors

    def get_by_id(self, floor_id: int) -> FloorEntity | None:
        floor = Floor.objects.filter(pk=floor_id).first()
        if floor:
            one_floor = FloorEntity(
                id=floor.id,
                storey=floor.storey,
                flats_count=floor.flats_count,
                status=floor.status,
                description=floor.description,
                entrance_id=floor.entrance_id,
                created_at=floor.created_at,
                last_update=floor.last_update,
            )
            return one_floor
        return None

    def get_by_entity(
        self, entity: str, entity_id: int
    ) -> list[FloorEntity] | None:
        query = Floor.objects
        if entity.lower() == "entrance":
            floors = query.filter(entrance_id=entity_id)
        elif entity.lower() == "bulding":
            floors = query.filter(entrance__building_id=entity_id)
        elif entity.lower() == "project":
            floors = query.filter(entrance__building__project_id=entity_id)
        else:
            return None
        list_of_floors = [
            FloorEntity(
                id=floor.id,
                storey=floor.storey,
                flats_count=floor.flats_count,
                status=floor.status,
                description=floor.description,
                entrance_id=floor.entrance_id,
                created_at=floor.created_at,
                last_update=floor.last_update,
            )
            for floor in floors
        ]
        return list_of_floors


class EntranceRepository:
    def get_all(self) -> list[EntranceEntity]:
        all_entrances = Entrance.objects.select_related("building")
        list_of_entrances = [
            EntranceEntity(
                id=entrance.id,
                number=entrance.number,
                flats_count=entrance.flats_count,
                floors_count=entrance.floors_count,
                building_id=entrance.building_id,
                created_at=entrance.created_at,
                last_update=entrance.last_update,
            )
            for entrance in all_entrances
        ]
        return list_of_entrances

    def get_by_id(self, entrance_id: int) -> EntranceEntity | None:
        entrance = Entrance.objects.filter(pk=entrance_id).first()
        if entrance:
            one_entrance = EntranceEntity(
                id=entrance.id,
                number=entrance.number,
                flats_count=entrance.flats_count,
                floors_count=entrance.floors_count,
                building_id=entrance.building_id,
                created_at=entrance.created_at,
                last_update=entrance.last_update,
            )
            return one_entrance
        return None

    def get_by_entity(
        self, entity: str, entity_id: int
    ) -> list[EntranceEntity] | None:
        query = Entrance.objects
        if entity.lower() == "building":
            entrances = query.filter(building_id=entity_id)
        elif entity.lower() == "project":
            entrances = query.filter(building__project_id=entity_id)
        else:
            return None
        list_of_entrances = [
            EntranceEntity(
                id=entrance.id,
                number=entrance.number,
                flats_count=entrance.flats_count,
                floors_count=entrance.floors_count,
                building_id=entrance.building_id,
                created_at=entrance.created_at,
                last_update=entrance.last_update,
            )
            for entrance in entrances
        ]
        return list_of_entrances
