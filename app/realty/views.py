from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from realty.models import Flat
from django.http import Http404


# Flat APIs

class FlatCreateAPIView(CreateAPIView):
    pass


class FlatListAPIView(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        area = serializers.DecimalField(max_digits=5, decimal_places=2)
        rooms_count = serializers.CharField()
        wc_count = serializers.IntegerField()
        floor = serializers.IntegerField()
        status = serializers.CharField()
        created_at = serializers.DateTimeField()
        last_update = serializers.DateTimeField()

    def get(self, request):
        flats = Flat.objects.all()
        serializer = FlatListAPIView.OutputSerializer(flats, many=True)
        return Response(serializer.data)
        


class FlatDetailAPIView(RetrieveAPIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        area = serializers.DecimalField(max_digits=5, decimal_places=2)
        rooms_count = serializers.CharField()
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

    def get(self, request, flat_id):
        flat = self.get_object(flat_id)
        serializer = FlatDetailAPIView.OutputSerializer(flat)
        return Response(serializer.data)



class FlatUpdateAPIView(UpdateAPIView):
    pass


class FlatDestroyAPIView(DestroyAPIView):
    pass
