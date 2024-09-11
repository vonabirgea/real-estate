from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


# Flat APIs

class FlatCreateAPIView(CreateAPIView):
    pass


class FlatListAPIView(ListAPIView):
    pass


class FlatDetailAPIView(RetrieveAPIView):
    pass


class FlatUpdateAPIView(UpdateAPIView):
    pass


class FlatDestroyAPIView(DestroyAPIView):
    pass
