from doctest import OutputChecker
from django.http import HttpResponse
from django.shortcuts import render
from .models import Adv

# Create your views here.


def index(request):
    advs = Adv.objects.all()
    return render(request, 'advs/index.html', {'advs': advs})
