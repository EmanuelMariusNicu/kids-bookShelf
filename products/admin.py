from django.contrib import admin
from .models import Product, Category

#Models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        "image"
    )

    


admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)