from django.shortcuts import render, redirect


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

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
