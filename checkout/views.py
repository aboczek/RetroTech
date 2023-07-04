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
        return redirect(reverse('items'))

    context = {
        'title': 'RetroTech Checkout!',
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)
