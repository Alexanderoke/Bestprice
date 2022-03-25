from django.db import models

# Create your models here.

class Product(models.Model):
  name =models.CharField(max_length=100)
  image = models.ImageField(blank=True, upload_to='product_images')
  price = models.DecimalField(max_digits=6, decimal_places=2)
  seller = models.TextField()
  platform_site = models.URLField(max_length=100, blank=True)

  def __str__(self):
    return self.name 