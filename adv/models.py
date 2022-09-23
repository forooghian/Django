from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Adv(models.Model):
    title = models.CharField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
