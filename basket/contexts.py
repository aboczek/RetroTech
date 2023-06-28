

def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0

    grand_total = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context