from django.shortcuts import render
from django.views.generic import ListView, DetailView
from library.models import Library


# Create your views here.
class LibraryLV(ListView):
    model = Library


class LibraryDV(DetailView):
    model = Library
