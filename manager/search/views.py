from django.shortcuts import render
from .models import City


def show_list(request):
    results = City.objects.all
    return render(request, "search/search_tags.html", {"showcity": results})
