from django.http import Http404
from realty.models import Building, Entrance, Flat


def get_all_objects(model):
    return model.objects.all()


def get_object_by_pk(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404


def count_entities(queryset):
    return queryset.count()


def get_flats_by_building(building_id):
    return Flat.objects.select_related("floor__entrance__building").filter(
        floor__entrance__building_id=building_id
    )


def count_flats_in_building(building_id):
    entrances = Entrance.objects.select_related("building").filter(
        building_id=building_id
    )
    total_flats_in_building = 0
    for entrance in entrances:
        total_flats_in_building += entrance.total_flats
    return total_flats_in_building


def get_buildings_by_project(project_id):
    buildings = Building.objects.select_related("project").filter(
        project_id=project_id
    )
    return buildings


def count_flats_in_project(project_id):
    entrances = Entrance.objects.select_related("building__project").filter(
        building__project_id=project_id
    )
    total_flats = 0
    for entrance in entrances:
        total_flats += entrance.total_flats
    return total_flats
