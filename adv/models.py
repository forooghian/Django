from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=255)


class Adv(models.Model):
    title = models.CharField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
