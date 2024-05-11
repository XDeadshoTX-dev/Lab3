"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)  # Product ID (AutoField)
    Product_name = models.CharField(max_length=100)  # Product name (String)
    Product_description = models.TextField()  # Product description (String)
    Product_image = models.ImageField(upload_to='Product_images/')  # Product image (Image)
    Product_stars = models.IntegerField()  # Product stars (Integer)
    Product_available_quantity = models.IntegerField()  # Product available quantity (Integer)
    Product_single_price = models.FloatField()  # Product single price (Float)

    def __str__(self):
        return self.Product_name
