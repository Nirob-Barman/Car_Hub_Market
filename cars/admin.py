from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Car)
admin.site.register(models.Comment)


# from django.contrib import admin
# from .models import Car, Comment


# class CarAdmin(admin.ModelAdmin):
#     list_display = ('name', 'brand', 'price', 'quantity', 'display_buyers')

#     def display_buyers(self, obj):
#         return ", ".join([buyer.username for buyer in obj.buyers.all()])

#     display_buyers.short_description = 'Buyers'


# admin.site.register(Car, CarAdmin)
# admin.site.register(Comment)
