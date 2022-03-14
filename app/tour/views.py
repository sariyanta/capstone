from core.models import Place
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class PlaceDetailView(DetailView):

    model = Place
    template_name = "tour/single_place.html"


class PlaceListView(ListView):

    model = Place
    template_name = "tour/list_place.html"
    context_object_name = "places"
