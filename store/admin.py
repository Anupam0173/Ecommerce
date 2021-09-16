from django.contrib import admin
from .models import customer, Product
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc']


admin.site.register(customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register()
