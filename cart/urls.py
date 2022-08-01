from django import urls
from django.urls import path
from django.urls.conf import include
from . import views

app_name='cart'

extra_patterns = [
    path('add/carts/<int:product_id>/', views.cart_add, name='cart_add'),
]

urlpatterns=[
   
    path ('add/',include(extra_patterns)),
    path ('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('ordersummary/',views.order_summary,name='order-summary'),
    path ('',views.cart_detail,name='cart_detail'),

]