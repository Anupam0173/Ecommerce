from django.contrib import admin
from .models import customer, product
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc']


admin.site.register(customer, CustomerAdmin)
admin.site.register(product, productAdmin)
# admin.site.register()
