from django.db import models
from django.contrib.auth.models import User


# class Customer(User):
#     mobile_no = models.CharField(
#         max_length=14, null=True, blank=True, default='SOME STRING')


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/images', default='')


# class order(models.Model):
#     customer = models.ForeignKey(
#         customer, on_delete=models.SET_NULL, null=True, blank=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)


# class orderItem(models.Model):
#     product = models.ForeignKey(
#         Product, on_delete=models.SET_NULL, null=True, blank=True)
#     order = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
