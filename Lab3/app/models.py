"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)  # Product ID (AutoField)
    Product_name = models.CharField(max_length=100, default="Unknown product")  # Product name (String)
    Product_description = models.TextField(default="Unknown description")  # Product description (String)
    Product_image_url = models.URLField(null=True, default=None) # Product url image (url)
    Product_image = models.ImageField(upload_to='Product_images/', null=True, default=None)  # Product image (Directory must be in app/Product_images/file.jpg)
    Product_stars = models.IntegerField(default=0)  # Product stars (Integer)
    Product_available_quantity = models.IntegerField(default=0)  # Product available quantity (Integer)
    Product_old_price = models.FloatField(default=0.0) # Product old price (Float)
    Product_single_price = models.FloatField(default=0.0)  # Product single price (Float)

    def __str__(self):
        return self.Product_name
