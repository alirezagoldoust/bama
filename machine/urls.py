from django.urls import path
from .views import List

urlpatterns=[
    path('', List)
]