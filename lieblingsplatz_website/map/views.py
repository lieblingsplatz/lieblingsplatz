from django.shortcuts import render
from map.models import Kita
from django.core import serializers
import logging

logger = logging.getLogger(__name__)


def home_page(request):
    kitas = serializers.serialize("python", Kita.objects.all())
    context = {"kitas": kitas}
    return render(request, 'home.html', context)


def list_kitas(request):
    kitas = serializers.serialize("python", Kita.objects.all())
    context = {"kitas": kitas}
    return render(request, 'list_kitas.html', context)

