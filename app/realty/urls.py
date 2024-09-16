from django.urls import path

from .views import (
    FlatListAPIView,
    FlatDetailAPIView,
)


urlpatterns = [
    path('flats', FlatListAPIView.as_view()),
    path('flat/<int:flat_id>/', FlatDetailAPIView.as_view()),
]
