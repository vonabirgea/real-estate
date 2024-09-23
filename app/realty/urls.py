from django.urls import path

from .views import (
    FlatListAPIView,
    FlatDetailAPIView,
    FloorDetailAPIView,
    FloorListAPIView,
)


urlpatterns = [
    path("flats", FlatListAPIView.as_view()),
    path("flats/<int:flat_id>/", FlatDetailAPIView.as_view()),
    path("floors/", FloorListAPIView.as_view()),
    path("floors/<int:floor_id>/", FloorDetailAPIView.as_view()),
]
