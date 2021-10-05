from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "image_field", "visit_count", "active")
    list_filter = ("title",)
    search_fields = ("title",)
    ordering = ("title", "price", "active")

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
