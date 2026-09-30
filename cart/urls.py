from django.urls import path
from . import  views

app_name = 'cart'
urlpatterns = [
    path('cartOverview/', views.cartoverview, name='cartOverview'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path("clear/", views.clear, name='clear'),
]