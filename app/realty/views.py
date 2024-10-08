from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from realty.selectors import (
    count_entities,
    count_flats_in_building,
    count_flats_in_project,
    get_all_objects,
    get_buildings_by_project,
    get_flats_by_building,
    get_object_by_pk,
)
from realty.models import Flat, Floor, Entrance, Building, Project
from drf_spectacular.utils import extend_schema, inline_serializer


class FlatListAPIView(APIView):
    class FlatListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        # area = serializers.DecimalField(max_digits=5, decimal_places=2)
        area = serializers.FloatField()
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor_id = serializers.IntegerField(source="floor.id")
        status = serializers.CharField()
        description = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

    @extend_schema(
        summary="Получение полного списка всех квартир.",
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
        flats = get_all_objects(model=Flat).select_related("floor")
        total_flats = count_entities(queryset=flats)
        serializer = FlatListAPIView.FlatListSerializer(flats, many=True)
        return Response({"total_flats": total_flats, "flats": serializer.data})


class FlatDetailAPIView(APIView):
    class FlatDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        area = serializers.FloatField()
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor_id = serializers.IntegerField(source="floor.id")
        status = serializers.CharField()
        description = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

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
        flat = get_object_by_pk(Flat, flat_id)
        serializer = FlatDetailAPIView.FlatDetailSerializer(flat)
        return Response(serializer.data)


class FloorListAPIView(APIView):
    class FloorListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        floor = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        entrance_id = serializers.IntegerField(source="entrance.id")

    @extend_schema(
        summary="Получение полного списка этажей.",
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
        floors = get_all_objects(model=Floor)
        total_floors = count_entities(floors)
        serializer = FloorListAPIView.FloorListSerializer(floors, many=True)
        return Response(
            {"total_floors": total_floors, "floors": serializer.data}
        )


class FloorDetailAPIView(APIView):
    class FloorDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        floor = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()
        entrance_id = serializers.IntegerField(source="entrance.id")

    @extend_schema(
        summary="Получение этажа по идентификатору floor_id.",
        description="API для получения конкретного этажа по floor_id",
        responses={
            status.HTTP_200_OK: FloorDetailSerializer(),
        },
        tags=["Этажи"],
    )
    def get(self, request, floor_id):
        floor = get_object_by_pk(Floor, floor_id)
        serializer = FloorDetailAPIView.FloorDetailSerializer(floor)
        return Response(serializer.data)


class EntranceListAPIView(APIView):
    class EntranceListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        flats_count = serializers.IntegerField()
        floors_count = serializers.IntegerField()
        building_id = serializers.IntegerField(source="building.id")

    @extend_schema(
        summary="Получение полного списка подъездов",
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
        entrances = get_all_objects(model=Entrance).select_related("building")
        total_entrances = count_entities(queryset=entrances)
        serializer = EntranceListAPIView.EntranceListSerializer(
            entrances, many=True
        )
        return Response(
            {"total_entrances": total_entrances, "entrances": serializer.data}
        )


class BuildingListAPIView(APIView):
    class BuildingListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        entrances_count = serializers.IntegerField()
        max_floors = serializers.IntegerField()
        project_id = serializers.IntegerField(source="project.id")
        commissioning_date = serializers.DateField()

    @extend_schema(
        summary="Получение полного списка зданий",
        description="API для получения списка зданий",
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
        buildings = get_all_objects(model=Building).select_related("project")
        total_buildings = count_entities(queryset=buildings)
        serializer = BuildingListAPIView.BuildingListSerializer(
            buildings, many=True
        )
        return Response(
            {"total_buildings": total_buildings, "buildings": serializer.data}
        )


class BuildingDetailAPIView(APIView):
    class BuildingDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        entrances_count = serializers.IntegerField()
        max_floors = serializers.IntegerField()
        project_id = serializers.IntegerField(source="project.id")
        commissioning_date = serializers.DateField()

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
        building = get_object_by_pk(Building, building_id)
        flats = get_flats_by_building(building_id)
        total_flats = count_flats_in_building(building_id)
        serializer = BuildingDetailAPIView.BuildingDetailSerializer(building)
        flats_serializer = FlatListAPIView.FlatListSerializer(flats, many=True)
        return Response(
            {
                "building_info": serializer.data,
                "total_flats": total_flats,
                "flats": flats_serializer.data,
            }
        )


class ProjectListAPIView(APIView):
    class ProjectListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        buildings_count = serializers.IntegerField()
        description = serializers.CharField()

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
        projects = get_all_objects(model=Project)
        total_projects = count_entities(projects)
        serializer = ProjectListAPIView.ProjectListSerializer(
            projects, many=True
        )
        return Response(
            {"total_projects": total_projects, "projects": serializer.data}
        )


class ProjectDetailAPIView(APIView):
    class ProjectDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        buildings_count = serializers.IntegerField()
        description = serializers.CharField()

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
        project = get_object_by_pk(model=Project, pk=project_id)
        buildings = get_buildings_by_project(project_id)
        serializer = ProjectDetailAPIView.ProjectDetailSerializer(project)
        buildings_serializer = BuildingListAPIView.BuildingListSerializer(
            buildings, many=True
        )
        total_flats_in_project = count_flats_in_project(project_id)
        return Response(
            {
                "project_info": serializer.data,
                "total_flats": total_flats_in_project,
                "project_buildings": buildings_serializer.data,
            }
        )
