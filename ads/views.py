from django.shortcuts import render
from django.http import HttpResponse
from .models import Ads, Car, Brand, Seller
import datetime

# Create your views here.
def ads_list(request):
    adss = Ads.objects.all()
    selected_car = request.GET.get('car')
    selected_min = request.GET.get('min')
    selected_max = request.GET.get('max')
    # Filtering data with queries
    if selected_car != None:
        adss = adss.filter(car__name=selected_car)
    if selected_min != None:
        adss = adss.filter(price__gte=selected_min)
    if selected_max != None:
        adss = adss.filter(price__lte=selected_max)
    return render(request, 'adspage/ads.html', {'adss':adss.order_by('-nardebam')})

def add_ads(request):
    if request.method == 'GET':
        return render(request, 'adspage/addads.html', {'cars':Car.objects.all(), 'brands':Brand.objects.all()})
    else:
        # print(request.POST.getlist())
        name = request.POST['name']
        user_type = request.POST['selected_type']
        selected_car = request.POST['selected_car']
        selected_brand = request.POST['selected_brand']
        color = request.POST['color']
        city = request.POST['city']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        kilometer = request.POST['kilometer']
        price = request.POST['price']
        year = request.POST['year']
        try:
            if request.POST['nardebam']:
                nardebam = True
        except:
            nardebam = False
        description = request.POST['description']
        try:
            seller = Seller.objects.get(name=name)
        except:
            seller = Seller.objects.create(name=name, phone_number=phone_number, verified=False, type=user_type)
        Ads.objects.create(
            car=Car.objects.get(name=selected_car),
            seller=seller,
            city=city,
            address=address,
            price=price,
            description=description,
            kilometer=kilometer,
            year=year,
            color=color,
            posting_time=datetime.datetime.today(),
            nardebam=nardebam,
        )
        return render(request, 'adspage/added.html', context={'Success':True})
