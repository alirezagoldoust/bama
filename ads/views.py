from django.shortcuts import render
from .models import Ads

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
    return render(request, 'adspage/ads.html', {'adss':adss})