from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Adv

# Create your views here.


def index(request):
    advs = Adv.objects.all()
    return render(request, 'advs/index.html', {'advs': advs})


def detail(request, adv_id):
    adv = get_object_or_404(Adv, pk=adv_id)
    return render(request, 'advs/detail.html', {'adv': adv})
