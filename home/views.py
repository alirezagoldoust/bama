from django.shortcuts import render, redirect
from django.http import HttpResponse
from ads.models import Car

def home_view(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        return render(request, "homepage/home.html", context={'cars':cars})
    else:
        # using query prameters
        selected_car = str(request.POST['selected_car'])
        selected_min = str(request.POST['minprice'])
        selected_max = str(request.POST['maxprice'])
        dest_url = '/ads/?car=' + selected_car
        if len(selected_min):
            dest_url = dest_url + '&min=' + selected_min
        if len(selected_max):
            dest_url = dest_url + '&max=' + selected_max
        return redirect(dest_url)