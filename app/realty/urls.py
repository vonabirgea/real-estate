from django.urls import path

from app.realty.views import (
    FlatCreateAPIView,
    FlatListAPIView,
    FlatDetailAPIView,
    FlatUpdateAPIView,
    FlatDestroyAPIView,
)


urlpatterns = [
    path('flats/', FlatListAPIView.as_view()),
    path('flat/<int:flat_id>/', FlatDetailAPIView.as_view()),
    path('flat_create/', FlatCreateAPIView.as_view()),
    path('flat_update/<int:flat_id>/', FlatUpdateAPIView.as_view()),
    path('flat_delete/<int:flat_id>/', FlatDestroyAPIView.as_view()),
]
