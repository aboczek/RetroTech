from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from items.models import Item
from .models import UserProfile
from checkout.models import Order
from .forms import ItemsForm, UserProfileForm


def home(request):
    """
    Home page.
    """

    items = Item.objects.all()

    context = {
        'title': 'RetroTech Home Page',
        'items': items,
    }

    return render(request, 'home/index.html', context)


def faq(request):
    """
    Frequently asked questions page.
    """

    context = {
        'title': 'RetroTech FAQ?'
    }

    return render(request, 'home/faq.html', context)


def track_your_order(request):
    """
    Track your order page to see tracking.
    """

    context = {
        'title': 'RetroTech Track your order.'
    }

    return render(request, 'home/tracking.html', context)


def profile(request):
    """
    User account.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        userprofileform = UserProfileForm(request.POST, instance=user_profile)
        if userprofileform.is_valid():
            userprofileform.save()
            messages.success(request, "Details have been updated successfully!")

    userprofileform = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    context = {
        'title': 'RetroTech User Account',
        'userprofileform': userprofileform,
        'orders': orders,
    }

    return render(request, 'home/profile.html', context)


def order_history(request, order_number):
    """
    Renders order history from user account/profile.
    """
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
        'title': 'RetroTech Order History',
    }

    return render(request, 'home/order-history.html', context)


@staff_member_required
def front_end_panel(request):
    """
    Front end admin panel.
    """

    # Create items
    items = Item.objects.all()
    items_form = ItemsForm()

    if request.method == 'POST':
        items_form = ItemsForm(request.POST, request.FILES)
        if items_form.is_valid():
            print(request.FILES)
            items_form.save()
            return redirect('profile')

    else:
        ItemsForm()

    context = {
        'title': 'RetroTech User Account',
        'items_form': items_form,
        'items': items,
    }

    return render(request, 'home/front.html', context)
