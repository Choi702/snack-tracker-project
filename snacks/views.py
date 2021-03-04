from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = snack




