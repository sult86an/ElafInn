from django.urls import path, include

from . import views


app_name = "virtual"
urlpatterns = [

    path("index/", views.index, name="index"),
    path("annual_offers/", views.annual_offer_list, name="annual_offer_list"),
    ]
