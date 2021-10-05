from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    is_read = models.BooleanField()

    def __str__(self):
        return self.subject

class Discription(models.Model):
    title = models.CharField(max_length=150)
    plase = models.TextField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):
        return self.title