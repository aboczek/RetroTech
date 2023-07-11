from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from items.models import Item
from .models import UserProfile, Newsletter
from checkout.models import Order
from .forms import ItemsForm, UserProfileForm, NewsletterForm


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
    newsletter = NewsletterForm()
    context = {
        'title': 'RetroTech FAQ?',
        'newsletter': newsletter,
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


@login_required
def front_end_panel(request):
    """
    Front end admin panel.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    items = Item.objects.all()
    items_form = ItemsForm()

    if request.method == 'POST':
        items_form = ItemsForm(request.POST, request.FILES)
        if items_form.is_valid():
            items_form.save()
            return redirect('front')

    else:
        items_form = ItemsForm()

    context = {
        'title': 'RetroTech User Account',
        'items_form': items_form,
        'items': items,
    }

    return render(request, 'home/front.html', context)


@login_required
def edit_item(request, item_id):
    """
    Editing items in front end admin panel.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    edit_item_form = ItemsForm()
    if request.method == 'POST':
        edit_item_form = ItemsForm(request.POST,
                                   request.FILES,
                                   instance=item)
        if edit_item_form.is_valid():
            edit_item_form.save()
            messages.success(request, 'Update was successful!')
            return redirect('front')
    edit_item_form = ItemsForm(instance=item)
    context = {
        'edit_item_form': edit_item_form,
        'title': 'RetroTech Lets edit boss!'
    }

    return render(request, 'home/edit-item.html', context)


@login_required
def delete_item(request, item_id):
    """
    Deleting items in front end admin panel.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, f'{ item.product_name} \
                      has was successfuly deleted.')
    return redirect('front')
