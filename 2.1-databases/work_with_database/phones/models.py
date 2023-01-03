from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    release_data = models.CharField(max_length=20)
    lte_exist = models.CharField(max_length=5)
    slug = models.CharField(max_length=40)
    img = models.CharField(max_length=200)