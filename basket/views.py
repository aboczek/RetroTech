from django.shortcuts import render


def basket(request):
    """
    Checkout page.
    """
    context = {
        'title': 'RetroTech Basket!',
    }

    return render(request, 'basket/basket.html', context)
