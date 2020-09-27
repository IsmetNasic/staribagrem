from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from .models import *



def index(request):
    return render(request, 'store/index.html')



def galerija(request):
    return render(request, 'store/galerija.html')


def jelovnik(request):
    return render(request, 'store/jelovnik.html')