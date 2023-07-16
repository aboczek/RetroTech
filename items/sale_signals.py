from decimal import Decimal
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Item


@receiver(pre_save, sender=Item)
def update_sale_price(sender, instance, **kwargs):
    """
    If Sale is True price of item will be reduced by 30%.
    """
    if instance.sale:
        instance.price = instance.price * Decimal('0.7')
    else:
        original_price = instance.get_original_price()
        instance.price = original_price
