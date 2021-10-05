from django.contrib.auth.models import User
from django.db import models
from eshop_products.models import Product
# Create your models here.

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    payment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.owner.get_username()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    def get_detail_sum(self):
        return self.count * self.price

    def __str__(self):
        return self.product.title