from django.urls import path
from . import views

urlpatterns = [
    path('add_cars/', views.add_cars, name='add_cars'),
    # path('car_detail/<int:car_id>/', views.CarDetailView.as_view, name='car_detail'),
    path('car_detail/<int:car_id>/', views.car_detail, name='car_detail'),
]
