from django.contrib import admin
from products.models import Product, Category, PickupPoint, Order, Subscription
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PickupPoint)
admin.site.register(Order)
admin.site.register(Subscription)