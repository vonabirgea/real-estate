from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer
from .selectors import (
    FlatsSelector,
    FloorsSelector,
    EntrancesSelector,
    BuildingsSelector,
    ProjectsSelector,
)


class FlatListAPIView(APIView):
    class FlatListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        area = serializers.FloatField()
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor_id = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

    selector = FlatsSelector()

    @extend_schema(
        summary="Получение всех существующих квартир.",
        description="API для получение полного списка квартир на сайте.",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="FlatListResponse",
                fields={
                    "total_flats": serializers.IntegerField(),
                    "flats": FlatListSerializer(many=True),
                },
            )
        },
        tags=["Квартиры"],
    )
    def get(self, request):
        total_flats, flats = self.selector.get_all()
        serializer = self.FlatListSerializer(flats, many=True)
        return Response({"total_flats": total_flats, "flats": serializer.data})


class FlatDetailAPIView(APIView):
    class FlatDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        area = serializers.FloatField()
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor_id = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

    selector = FlatsSelector()

    @extend_schema(
        summary="Получение конкретной квартиры по её идентификатору flat_id.",
        description="""API для получения конкретной квартиры
            по её уникальному иднетификатору flat_id.""",
        responses={
            status.HTTP_200_OK: FlatDetailSerializer(),
        },
        tags=["Квартиры"],
    )
    def get(self, request, flat_id):
        flat = self.selector.get_one(flat_id)
        serializer = self.FlatDetailSerializer(flat)
        return Response(serializer.data)


class FlatListByEntityAPIView(APIView):
    class FlatListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        area = serializers.FloatField()
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor_id = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

    selector = FlatsSelector()

    @extend_schema(
        summary="Получение квартир в разных сущностях",
        description="""API для получения списка квартир, принадлежащих различным
          entity (floor, entrance, building, project) через указание
          entity и её entity_id""",
        tags=["Квартиры"],
    )
    def get(self, request, entity, entity_id):
        total_flats, flats = self.selector.get_by_entity(entity, entity_id)
        serializer = self.FlatListSerializer(flats, many=True)
        return Response({"total_flats": total_flats, "flats": serializer.data})


class FloorListAPIView(APIView):
    class FloorListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        storey = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        entrance_id = serializers.IntegerField()

    selector = FloorsSelector()

    @extend_schema(
        summary="Получение всех существующих этажей.",
        description="API для получение полного списка этажей",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="FloorListResponse",
                fields={
                    "total_floors": serializers.IntegerField(),
                    "floors": FloorListSerializer(many=True),
                },
            )
        },
        tags=["Этажи"],
    )
    def get(self, request):
        total_floors, floors = self.selector.get_all()
        serializer = self.FloorListSerializer(floors, many=True)
        return Response(
            {"total_floors": total_floors, "floors": serializer.data}
        )


class FloorDetailAPIView(APIView):
    class FloorDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        storey = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        entrance_id = serializers.IntegerField(source="entrance.id")

    selector = FloorsSelector()

    @extend_schema(
        summary="Получение этажа по идентификатору floor_id.",
        description="API для получения конкретного этажа по floor_id",
        responses={
            status.HTTP_200_OK: FloorDetailSerializer(),
        },
        tags=["Этажи"],
    )
    def get(self, request, floor_id):
        floor = self.selector.get_one(floor_id)
        floor_serializer = self.FloorDetailSerializer(floor)
        return Response(floor_serializer.data)


class FloorListByEntityAPIView(APIView):
    class FloorListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        storey = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        entrance_id = serializers.IntegerField()

    selector = FloorsSelector()

    @extend_schema(
        summary="Получение этажей в разных сущностях",
        description="""API для получения списка этажей, принадлежащих различным
        entity (entrance, building, project) через указание entity и её entity_id""",
        tags=["Этажи"],
    )
    def get(self, request, entity, entity_id):
        total_floors, floors = self.selector.get_by_entity(entity, entity_id)
        serializer = self.FloorListSerializer(floors, many=True)
        return Response(
            {"total_floors": total_floors, "floors": serializer.data}
        )


class EntranceListAPIView(APIView):
    class EntranceListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        floors_count = serializers.IntegerField()
        building_id = serializers.IntegerField()

    selector = EntrancesSelector()

    @extend_schema(
        summary="Получение всех существующих подъездов",
        description="API для получения списка подъездов",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="EntranceListResponse",
                fields={
                    "total_entrances": serializers.IntegerField(),
                    "entrances": EntranceListSerializer(many=True),
                },
            )
        },
        tags=["Подъезды"],
    )
    def get(self, request):
        num_of_entrances, entrances = self.selector.get_all()
        serializer = self.EntranceListSerializer(entrances, many=True)
        return Response(
            {"total_entrances": num_of_entrances, "entrances": serializer.data}
        )


class EntranceDetailAPIView(APIView):
    class EntranceDetailSerialiser(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        floors_count = serializers.IntegerField()
        building_id = serializers.IntegerField()

    selector = EntrancesSelector()

    @extend_schema(
        summary="Получение подъезда по его entrance_id",
        description="API для получения конкретного подъезда",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="EntranceDetailResponse",
                fields={
                    "entrance_info": EntranceDetailSerialiser(),
                    "total_flats": serializers.IntegerField(),
                    "flats": FlatListAPIView.FlatListSerializer(many=True),
                },
            )
        },
        tags=["Подъезды"],
    )
    def get(self, request, entrance_id):
        entrance = self.selector.get_one(entrance_id)
        serializer = self.EntranceDetailSerialiser(entrance)
        return Response(serializer.data)


class EntranceListByEntityAPIView(APIView):
    class EntranceListSerialiser(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        floors_count = serializers.IntegerField()
        building_id = serializers.IntegerField()

    selector = EntrancesSelector()

    @extend_schema(
        summary="Получение подъездов в разных сущностях.",
        description="""API для получения списка подъездов, принадлежащих различным
        сущностям (building, project) через указание entity и entity_id""",
        tags=["Подъезды"],
    )
    def get(self, request, entity, entity_id):
        total_entrances, entrances = self.selector.get_by_entity(
            entity, entity_id
        )
        serialiser = self.EntranceListSerialiser(entrances, many=True)
        return Response(
            {"total_entrances": total_entrances, "entrances": serialiser.data}
        )


class BuildingListAPIView(APIView):
    class BuildingListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        entrances_count = serializers.IntegerField()
        max_floors = serializers.IntegerField()
        project_id = serializers.IntegerField()
        commissioning_date = serializers.DateField()

    selector = BuildingsSelector()

    @extend_schema(
        summary="Получение всех существующих зданий",
        description="API для получения полного списка зданий",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="BuildingListResponse",
                fields={
                    "total_buildings": serializers.IntegerField(),
                    "buidings": BuildingListSerializer(many=True),
                },
            )
        },
        tags=["Здания (корпуса)"],
    )
    def get(self, request):
        total_buildings, buildings = self.selector.get_all()
        serializer = self.BuildingListSerializer(buildings, many=True)
        return Response(
            {"total_buildings": total_buildings, "buildings": serializer.data}
        )


class BuildingDetailAPIView(APIView):
    class BuildingDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        entrances_count = serializers.IntegerField()
        max_floors = serializers.IntegerField()
        project_id = serializers.IntegerField()
        commissioning_date = serializers.DateField()

    selector = BuildingsSelector()

    @extend_schema(
        summary="Получение здания по его building_id",
        description="API для получения конкретного здания",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="BuildingDetailResponse",
                fields={
                    "building_info": BuildingDetailSerializer(),
                    "total_flats": serializers.IntegerField(),
                    "flats": FlatListAPIView.FlatListSerializer(many=True),
                },
            )
        },
        tags=["Здания (корпуса)"],
    )
    def get(self, request, building_id):
        building = self.selector.get_one(building_id)
        serializer = self.BuildingDetailSerializer(building)
        return Response(serializer.data)


class BuildingListByEntityAPIView(APIView):
    class BuildingListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        entrances_count = serializers.IntegerField()
        max_floors = serializers.IntegerField()
        project_id = serializers.IntegerField()
        commissioning_date = serializers.DateField()

    selector = BuildingsSelector()

    @extend_schema(
        summary="Получение здания по сущности проекта",
        description="API для получения списка зданий, принадлежащих entity прокта.",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="BuildingListResponse",
                fields={
                    "total_buildings": serializers.IntegerField(),
                    "buidings": BuildingListSerializer(many=True),
                },
            )
        },
        tags=["Здания (корпуса)"],
    )
    def get(self, request, entity, entity_id):
        num_of_buildings, buildings = self.selector.get_by_entity(
            entity, entity_id
        )
        serializer = self.BuildingListSerializer(buildings, many=True)
        return Response(
            {"num_of_buildings": num_of_buildings, "buildings": serializer.data}
        )


class ProjectListAPIView(APIView):
    class ProjectListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        buildings_count = serializers.IntegerField()
        description = serializers.CharField()

    selector = ProjectsSelector()

    @extend_schema(
        summary="Получение списка проектов",
        description="API для получения списка проектов",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="ProjectListresponse",
                fields={
                    "total_projects": serializers.IntegerField(),
                    "projects": ProjectListSerializer(many=True),
                },
            )
        },
        tags=["Проекты"],
    )
    def get(self, request):
        total_projects, projects = self.selector.get_all()
        serializer = self.ProjectListSerializer(projects, many=True)
        return Response(
            {"total_projects": total_projects, "projects": serializer.data}
        )


class ProjectDetailAPIView(APIView):
    class ProjectDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        buildings_count = serializers.IntegerField()
        description = serializers.CharField()

    selector = ProjectsSelector()

    @extend_schema(
        summary="Получение информации о проекте",
        description="API для получения информации о проекте по project_id",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="ProjectDetailResponse",
                fields={
                    "project_info": ProjectDetailSerializer(),
                    "total_flats": serializers.IntegerField(),
                    "project_buildings": BuildingListAPIView.BuildingListSerializer(
                        many=True
                    ),
                },
            )
        },
        tags=["Проекты"],
    )
    def get(self, response, project_id):
        project = self.selector.get_one(project_id)
        serializer = self.ProjectDetailSerializer(project)
        return Response(serializer.data)
