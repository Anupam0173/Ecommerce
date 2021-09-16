from django.urls import path
from store import views
urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('view_product/<int:id>', views.view_product, name='view_product')
]
