from django.db import models
from eshop_products.models import upload_image_path

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title
