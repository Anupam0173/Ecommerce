from django.urls import path
from store import views
urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('view_product/<int:id>', views.view_product, name='view_product'),
    path('logout/', views.user_logout, name='logout'),
]
