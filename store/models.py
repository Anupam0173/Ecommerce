from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField(max_length=100)
    is_company_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.name
