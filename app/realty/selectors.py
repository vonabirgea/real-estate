from django.http import Http404


def get_all_objects(model):
    return model.objects.all()


def get_object_by_pk(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404


def count_entities(queryset):
    return len(queryset)
