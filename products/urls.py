from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),

    path('product-list/', views.product_list, name='product-list'),
    path('products/category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('products/create/', views.product_create, name='product-create'),
    path('product-search/', views.product_search, name='product-search'),
    path('products/<int:pk>/update/', views.product_update, name='product-update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product-delete'),

    path('order-list/', views.order_list, name='order-list'),
    path('place/order/<int:product_id>/', views.place_order, name='place-order'),
    path('update-order-status/<int:order_id>/', views.update_order_status, name='update-order-status'),
    path('sells/', views.sells_page, name='sells-page'),


    path('category-list/', views.category_list, name='category-list'),
    path('categories/create/', views.category_create, name='category-create'),

    path('pickup-list/', views.pickup_list, name='pickup-list'),
    path('pickup-points/create/', views.pickup_create, name='pickup-point-create'),

]