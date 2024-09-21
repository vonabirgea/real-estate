from django.http import Http404


def get_all_objects(model):
    return model.objects.all()


def get_object_by_pk(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404


def get_floor_by_flat(flat):
    get_floor_by_flat.short_description = "Этаж"
    return flat.floor.floor
