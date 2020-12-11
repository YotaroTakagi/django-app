from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Mahjong

def index (request):
    currentTime = timezone.now()
    return render(request, 'mahjong/index.html', {'time' : currentTime})
