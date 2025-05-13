from django.contrib import admin

from products.models import Product, Category, PickupPoint, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PickupPoint)
admin.site.register(Order)