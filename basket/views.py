from django.shortcuts import render, redirect, reverse, HttpResponse


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


def update_basket(request, item_id):
    """
    updates basket content.
    """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        if quantity > 0:
            basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Remove content from basket.
    """
    try:
        basket = request.session.get('basket', {})

        if item_id in list(basket.keys()):
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as er:
        return HttpResponse(status=500)
