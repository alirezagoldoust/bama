from django.contrib.admin import ModelAdmin, register
from .models import Brand, Car, Ads, Seller

# Register your models here.

@register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ['name']

@register(Car)
class CarAdmin(ModelAdmin):
    list_display = ['name', 'brand']

@register(Ads)
class AdsAdmin(ModelAdmin):
    list_display = ['car', 'seller']

@register(Seller)
class SellerAdmin(ModelAdmin):
    list_display = ['name']