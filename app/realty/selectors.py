from django.http import Http404
from .repositories import (
    FlatRepository,
    FloorRepository,
    EntranceRepository,
    BuildingRepository,
    ProjectRepository,
)
from .entities import (
    FlatEntity,
    FloorEntity,
    EntranceEntity,
    BuildingEntity,
    ProjectEntity,
)


class FlatsSelector:
    repository = FlatRepository()

    def get_all(self) -> tuple[int, list[FlatEntity]]:
        flats = self.repository.get_all()

        num_of_flats = len(flats)
        return num_of_flats, flats

    def get_one(self, flat_id: int) -> FlatEntity:
        flat = self.repository.get_by_id(flat_id)
        if not flat:
            raise Http404(f"Квартиры с id={flat_id} не существует.")
        return flat

    def get_by_entity(
        self, entity, entity_id: int
    ) -> tuple[int, list[FlatEntity]]:
        flats = self.repository.get_by_entity(entity, entity_id)
        if not flats:
            raise Http404(
                f"Сочетанию entity={entity} и entity_id={entity_id} не принадлежит ни одна квартира."
            )
        total_flats = len(flats)
        return total_flats, flats


class FloorsSelector:
    repository = FloorRepository()

    def get_all(self) -> tuple[int, list[FloorEntity]]:
        floors = self.repository.get_all()

        num_of_floors = len(floors)
        return num_of_floors, floors

    def get_one(self, floor_id: int) -> FloorEntity:
        floor = self.repository.get_by_id(floor_id)
        if not floor:
            raise Http404(f"Этажа с id={floor_id} не существует.")
        return floor

    def get_by_entity(
        self, entity: str, entity_id: int
    ) -> tuple[int, list[FloorEntity]]:
        floors = self.repository.get_by_entity(entity, entity_id)
        if not floors:
            raise Http404(
                f"Сочетанию entity={entity} и entity_id={entity_id} не принадлежит ни один этаж."
            )
        total_floors = len(floors)
        return total_floors, floors


class EntrancesSelector:
    repository = EntranceRepository()

    def get_all(self) -> tuple[int, list[EntranceEntity]]:
        entrances = self.repository.get_all()
        num_of_entrances = len(entrances)
        return num_of_entrances, entrances

    def get_one(self, entrance_id: int) -> EntranceEntity:
        entrance = self.repository.get_by_id(entrance_id)
        if not entrance:
            raise Http404(f"Подъезда с id={entrance_id} не существует.")
        return entrance

    def get_by_entity(
        self, entity: str, entity_id: int
    ) -> tuple[int, list[EntranceEntity]]:
        entrances = self.repository.get_by_entity(entity, entity_id)
        if not entrances:
            raise Http404(
                f"Сочетанию entity={entity} и entity_id={entity_id} не соответствует ни один подъезд"
            )
        total_entrances = len(entrances)
        return total_entrances, entrances


class BuildingsSelector:
    repository = BuildingRepository()

    def get_all(self) -> tuple[int, list[BuildingEntity]]:
        buildings = self.repository.get_all()
        num_of_buildings = len(buildings)
        return num_of_buildings, buildings

    def get_one(self, building_id: int) -> BuildingEntity:
        building = self.repository.get_by_id(building_id)
        if not building:
            raise Http404(f"Здания с id={building_id} не существует.")
        return building

    def get_by_entity(
        self, entity: str, entity_id: int
    ) -> tuple[int, list[BuildingEntity]]:
        buildings = self.repository.get_by_entity(entity, entity_id)
        if not buildings:
            raise Http404(
                f"Сочетанию entity={entity} и entity_id={entity_id} не соответствует ни одно здание."
            )
        num_of_buildings = len(buildings)
        return num_of_buildings, buildings


class ProjectsSelector:
    repository = ProjectRepository()

    def get_all(self) -> tuple[int, list[ProjectEntity]]:
        projects = self.repository.get_all()
        num_of_projects = len(projects)
        return num_of_projects, projects

    def get_one(self, project_id: int) -> ProjectEntity:
        project = self.repository.get_by_id(project_id)
        if not project:
            raise Http404(f"Проекта с id={project_id} не существует.")
        return project
