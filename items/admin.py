from django.contrib import admin
from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    """
    Category model.
    """
    list_display = (
        'name',
        'frontend_name',
    )


class ItemAdmin(admin.ModelAdmin):
    """
    Item Model.
    """
    list_display = (
        'sku_number',
        'product_name',
        'product_model',
        'product_description',
        'quantity',
        'price',
        'sale',
        'featured',
        'image',
    )

    ordering = ('sku_number',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
