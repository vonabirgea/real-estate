from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from realty.models import Flat
from django.http import Http404
from drf_spectacular.utils import extend_schema


class FlatListAPIView(APIView):
    class FlatListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        area = serializers.DecimalField(max_digits=5, decimal_places=2)
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor = serializers.IntegerField()
        status = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

    @extend_schema(
        summary="Получение полного списка всех квартир.",
        description="""Очень удобное api для получение полного списка 
            квартир которые когда-либол были добавлены на сайт.""",
        responses={
            status.HTTP_200_OK: FlatListSerializer,
        },
    )
    def get(self, request):
        flats = Flat.objects.all()
        serializer = FlatListAPIView.FlatListSerializer(flats, many=True)
        return Response(serializer.data)


class FlatDetailAPIView(APIView):
    class FlatDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        area = serializers.DecimalField(max_digits=5, decimal_places=2)
        rooms_count = serializers.IntegerField()
        wc_count = serializers.IntegerField()
        floor = serializers.IntegerField()
        status = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

    def get_object(self, flat_id):
        try:
            return Flat.objects.get(pk=flat_id)
        except Flat.DoesNotExist:
            raise Http404

    @extend_schema(
        summary="Получение конкретной квартиры по её идентификатору flat_id.",
        description="""Очень удобное api для получения конкретной квартиры
            по её уникальному иднетификатору flat_id.""",
        responses={
            status.HTTP_200_OK: FlatDetailSerializer,
        },
    )
    def get(self, request, flat_id):
        flat = self.get_object(flat_id)
        serializer = FlatDetailAPIView.FlatDetailSerializer(flat)
        return Response(serializer.data)
