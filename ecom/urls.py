from django.urls import path

from . import views

app_name = 'ecom'
urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:slug>',views.detail,name='detail'),
    path('addToCart/',views.addToCart,name='addToCart'),
]