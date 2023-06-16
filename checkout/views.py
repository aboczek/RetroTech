from django.shortcuts import render


def checkout(request):
    """
    Checkout page.
    """
    context = {
        'title': 'RetroTech Checkout!',
    }

    return render(request, 'checkout/checkout.html', context)
