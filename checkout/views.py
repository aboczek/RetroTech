from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from basket.contexts import basket_contents
from items.models import Item
from .models import Order, OrderLineItem
from .forms import OrderForm
import stripe
import json



@require_POST
def cache_checkout_data(request):
    """
    Caching checkout data.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_details': request.POST.get('save_details'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, We cannot process your \
                        payment, Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Checkout page.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county_state': request.POST['county_state'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, quantity in basket.items():
                try:
                    item = Item.objects.get(id=item_id)
                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            item=item,
                            quantity=quantity,
                        )
                        order_line_item.save()
                except Item.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your basket cannot be \
                              found in your database, \
                                  Please contact us for help!"
                    ))
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_details'] = 'save-details' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There is error in your details, \
                            Please check your data.")
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'You have nothing added to basket.')
            return redirect(reverse('all_items'))

    order_form = OrderForm()
    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing, \
                          set it up in your environment.')

    context = {
        'title': 'RetroTech Checkout!',
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Renders checkout success if payment was successful.
    """
    save_details = request.session.get('save_details')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    context = {
        'title': 'RetroTech Success!',
        'order': order
    }

    return render(request, 'checkout/checkout-success.html', context)
