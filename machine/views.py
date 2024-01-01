from django.shortcuts import render
from ads.models import Car

def List(request):
    return render(request, 'machinepage/machine.html', {'cars':Car.objects.all()})