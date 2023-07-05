from django.shortcuts import get_object_or_404
from items.models import Item


def basket_contents(request):
    """
    Lets content of basket and quantity
    and grand total to be rendered in all templates.
    """
    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item,
        })

    grand_total = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context
