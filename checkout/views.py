from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404,
                              HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string


from basket.contexts import basket_contents
from items.models import Item
from home.models import UserProfile
from home.forms import UserProfileForm
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

    # Prefiling form with details saved in user account/profile.
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': user_profile.user.get_full_name(),
                'email': user_profile.user.email,
                'phone_number': user_profile.default_phone_number,
                'country': user_profile.default_country,
                'postcode': user_profile.default_postcode,
                'town_or_city': user_profile.default_town_or_city,
                'street_address1': user_profile.default_street_address1,
                'street_address2': user_profile.default_street_address2,
                'county_state': user_profile.default_county_state,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

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

    cust_email = order.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_details:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county_state': order.county_state,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    else:
        order.save()

    messages.success(request, f'Order successfully processed! \
                      Your order number is {order_number}. A \
                          confirmation email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    context = {
        'title': 'RetroTech Success!',
        'order': order
    }

    return render(request, 'checkout/checkout-success.html', context)
