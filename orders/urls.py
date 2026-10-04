from django.urls import path


from . import views

app_name = 'orders'
urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("add-address/",views.add_address,name="add_address"),
    path('order-success/<int:pk>/', views.order_success, name='order_success'),
]