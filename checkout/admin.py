from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    """
    TabularInLine for OrderLineItem.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    OrderAdmin for Order model.
    """
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total',
                       'original_basket', 'stripe_pid')
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county_state', 'order_total',
              'grand_total', 'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
