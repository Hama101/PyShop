from django.db import models as m

# Product table
class Product(m.Model):
    name = m.CharField(max_length=255)
    price = m.FloatField()
    stock = m.IntegerField()
    image_url = m.CharField(max_length=2083)

#offer table
class Offer(m.Model):
    code = m.CharField(max_length=10)
    description = m.CharField(max_length=255)
    discount = m.FloatField()
