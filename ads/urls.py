from django.urls import path
from .views import ads_list, add_ads

urlpatterns=[
    path('', ads_list),
    path('add', add_ads),
]