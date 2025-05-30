from django import forms
from .models import Product, Category, Order, PickupPoint, Subscription


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'expired_at', 'image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'icon']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'quantity', 'pickup_point']

class PickupPointForm(forms.ModelForm):
    class Meta:
        model = PickupPoint
        fields = ['name', 'address']

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'email']