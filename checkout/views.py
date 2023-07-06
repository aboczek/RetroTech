from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    Checkout page.
    """
    order_form = OrderForm()
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, 'You have nothing added to basket.')
        return redirect(reverse('all_items'))

    context = {
        'title': 'RetroTech Checkout!',
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NQwPPKXtaWpDhDxlnJtpmTVy5JrBP1o2lsH05CSKTpOvbQE1lbXMqTAE7rmpnmViowJkWBw7vX0T2mnccCe1DKG00mvjwQj8R',
        'client_secret': 'testing',
    }

    return render(request, 'checkout/checkout.html', context)
