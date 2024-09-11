from django.urls import path

from .views import (
    FlatCreateAPIView,
    FlatListAPIView,
    FlatDetailAPIView,
    FlatUpdateAPIView,
    FlatDestroyAPIView,
)


urlpatterns = [
    path('flats', FlatListAPIView.as_view()),
    path('flat/create/', FlatCreateAPIView.as_view()),
    path('flat/<int:flat_id>/', FlatDetailAPIView.as_view()),
    path('flat/<int:flat_id>/update/', FlatUpdateAPIView.as_view()),
    path('flat/<int:flat_id>/delete/', FlatDestroyAPIView.as_view()),
]
