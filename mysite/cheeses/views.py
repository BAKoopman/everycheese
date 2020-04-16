from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Cheese
from django.contrib.auth.mixins import LoginRequiredMixin

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = [
        "name",
        "description",
        "firmness",
        "country_of_origin"
    ]
class CheeseUpdateView(LoginRequiredMixin,UpdateView):
    model = Cheese
    fields = [
        "name",
        "description",
        "firmness",
        "country_of_origin"
    ]
    action = "Update"