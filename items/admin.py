from django.contrib import admin
from .models import Category, Item, SellToUs


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
        'image_one',
        'image_two',
        'image_three',
    )

    ordering = ('sku_number',)


class SellToUsAdmin(admin.ModelAdmin):
    """
    Sell to us model.
    """
    list_display = (
        'full_name',
        'email',
        'brand',
        'model',
        'grade',
        'description',
        'sell_image_one',
        'sell_image_two',
        'sell_image_three',
    )

    ordering = ('full_name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(SellToUs, SellToUsAdmin)
