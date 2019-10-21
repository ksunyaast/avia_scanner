import time
import random

from django.core.serializers import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'
    form = cache.get_or_set('search_ticket', SearchTicket(), 10)

    # key = 'search_ticket'
    # timeout = 10
    # form = cache.get(key)
    # if form is None:
    #     form = SearchTicket()
    #     cache.set(key, form, timeout)

    context = {
        'form': form
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    results = []
    cities = City.objects.all().order_by('name')
    for city in cities:
        results.append(city.name)
    return JsonResponse(results, safe=False)
