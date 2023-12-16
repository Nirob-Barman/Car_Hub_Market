from django.shortcuts import render
from cars.models import Car
from brands.models import Brands


def home(request, brand_name=None):
    cars = Car.objects.all()
    brands = Brands.objects.all()

    brandName = brand_name

    if brand_name:
        cars = cars.filter(brand__name=brand_name)

    return render(request, 'home.html', {'cars': cars, 'brands': brands, 'brandName': brandName})
