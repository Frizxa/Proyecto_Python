from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar(request):
    return HttpResponse(f'buenas tardes martin. la hora es: {datetime.now()}')



# Create your views here.
