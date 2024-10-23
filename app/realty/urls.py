from django.urls import path

from .views import (
    BuildingDetailAPIView,
    BuildingListAPIView,
    EntranceDetailAPIView,
    EntranceListAPIView,
    FlatListAPIView,
    FlatDetailAPIView,
    FlatsOnFloorListAPIView,
    FloorDetailAPIView,
    FloorListAPIView,
    ProjectDetailAPIView,
    ProjectListAPIView,
)


urlpatterns = [
    path("flats/", FlatListAPIView.as_view()),
    path("flats/<int:flat_id>/", FlatDetailAPIView.as_view()),
    path("floors/", FloorListAPIView.as_view()),
    path("floors/<int:floor_id>/", FloorDetailAPIView.as_view()),
    path("floors/<int:floor_id>/flats/", FlatsOnFloorListAPIView.as_view()),
    path("entrances/", EntranceListAPIView.as_view()),
    path("entrances/<int:entrance_id>/", EntranceDetailAPIView.as_view()),
    path("buildings/", BuildingListAPIView.as_view()),
    path("buildings/<int:building_id>/", BuildingDetailAPIView.as_view()),
    path("projects/", ProjectListAPIView.as_view()),
    path("projects/<int:project_id>/", ProjectDetailAPIView.as_view()),
]
