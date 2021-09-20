from django.urls import path
from .import views

urlpatterns = [
    path('advert/', views.advertisement_list, name="advertisement_list")
]
