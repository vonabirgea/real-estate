from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from realty.selectors import count_entities, get_all_objects, get_object_by_pk
from realty.models import Flat, Floor
from drf_spectacular.utils import extend_schema, inline_serializer


class FlatListAPIView(APIView):
    class FlatListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        # area = serializers.DecimalField(max_digits=5, decimal_places=2)
        area = serializers.FloatField()
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor = serializers.IntegerField(source="floor.floor")
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
        # area = serializers.DecimalField(max_digits=5, decimal_places=2)
        area = serializers.FloatField()
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor = serializers.IntegerField(source="floor.floor")
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
        flats_on_floor = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()

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
        flats_on_floor = serializers.IntegerField()
        status = serializers.CharField()
        description = serializers.CharField()

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
