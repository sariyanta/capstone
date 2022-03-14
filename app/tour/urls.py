from django.urls import path

from tour.views import PlaceDetailView, PlaceListView

urlpatterns = [
    path("", PlaceListView.as_view(), name="place-list"),
    path("<slug:slug>", PlaceDetailView.as_view(), name="place-detail"),
]
