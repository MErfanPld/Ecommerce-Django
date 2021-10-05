from django.db import models
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    copy_right = models.TextField(max_length=1000, blank=True)
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    link_twitter = models.URLField()
    link_facebook = models.URLField()
    link_behance = models.URLField()
    link_globe = models.URLField()

    def __str__(self):
        return self.title
