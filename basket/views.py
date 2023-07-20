from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from items.models import Item


def view_basket(request):
    """
    Checkout page.
    """
    context = {
        'title': 'RetroTech Basket',
    }

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):
    """
    Adds quantity of individual item to basket.
    """

    item = get_object_or_404(Item, pk=item_id)
    quantity_str = request.POST.get('quantity', '')
    quantity = int(quantity_str) if quantity_str else 0
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if quantity <= 0:
        messages.error(request, 'Sorry, you can order must be 1 or \
                        more. Please try again.')
    elif quantity > 99:
        messages.error(request, 'Sorry, the maximum order per \
                            selected item is 99.')
    elif item_id in list(basket.keys()):
        if basket[item_id] + quantity > 99:
            messages.error(request, 'Sorry, the maximum order per \
                            selected item is 99.')
        else:
            basket[item_id] += quantity
            messages.success(request, f'{item.product_name} has been \
                              updated to quantity of {basket[item_id]}.')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{item.product_name} with quantity of \
                          {quantity} has been added to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """
    updates basket content.
    """

    item = get_object_or_404(Item, pk=item_id)
    basket = request.session.get('basket', {})
    quantity_input = request.POST.get('quantity')

    if quantity_input.isdigit():
        quantity = int(request.POST.get('quantity'))

        if quantity > 99:
            messages.error(request, 'Sorry, the maximum quantity per \
                            selected item is 99.')
        elif quantity >= 1:
            basket[item_id] = quantity
            messages.success(request, f'{item.product_name} has been \
                              updated to {basket[item_id]}.')
        else:
            basket.pop(item_id)
            messages.success(request, f'{item.product_name} has been \
                              removed from basket.')
    elif quantity_input.startswith('-'):
        messages.error(request, 'Sorry, the quantity of \
                        product has to be 1 or more.')

    elif not quantity_input.isdigit():
        messages.error(request, 'Product quantity has to be positive number.')

    else:
        messages.error(request, 'Please enter a whole number.')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Remove content from basket.
    """

    item = get_object_or_404(Item, pk=item_id)

    try:
        basket = request.session.get('basket', {})

        if item_id in list(basket.keys()):
            basket.pop(item_id)
            messages.success(request, f'{item.product_name} has been removed.')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as err:
        return HttpResponse(status=500)
