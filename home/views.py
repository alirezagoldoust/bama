from django.shortcuts import render, redirect
from django.http import HttpResponse
from ads.models import Car

def home_view(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        return render(request, "homepage/home.html", context={'cars':cars})
    else:
        # using query prameters
        selected_car = request.POST['selected_car']
        selected_min = request.POST['minprice']
        selected_max = request.POST['maxprice']
        print([selected_car, selected_max, selected_min])
        dest_url = '/ads/?'
        if selected_car != '':
            dest_url = dest_url + 'car=' + selected_car
        if selected_min != '':
            dest_url = dest_url + '&min=' + selected_min
        if selected_max != '':
            dest_url = dest_url + '&max=' + selected_max
        return redirect(dest_url)