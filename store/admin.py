from django.contrib import admin
from .models import Product
# Register your models here.


# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['mobile_no', 'email', 'first_name', 'last_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc']


# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register()
