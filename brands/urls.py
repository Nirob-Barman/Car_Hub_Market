from django.urls import path
from . import views

urlpatterns = [
    path('add_brands/', views.add_brands, name='add_brands'),
]
