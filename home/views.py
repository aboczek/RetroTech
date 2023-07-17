from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from items.models import Item
from items.models import SellToUs
from checkout.models import Order
from .models import UserProfile, Newsletter
from .forms import ItemsForm, UserProfileForm, NewsletterForm


def home(request):
    """
    Home page.
    """
    items_sale = Item.objects.filter(sale=True)
    items_featured = Item.objects.filter(featured=True)

    context = {
        'title': 'RetroTech Home Page',
        'items_sale': items_sale,
        'items_featured': items_featured
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
            messages.success(request, "Details have \
                              been updated successfully!")

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


def terms_conditions(request):
    """
    Terms and conditions.
    """

    context = {
        'title': 'RetroTech Terms and Conditions',
    }

    return render(request, 'home/terms-conditions.html', context)


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
            messages.success(request, 'Product has been created!')
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


@login_required
def newsletter_email(request):
    """
    Rendering subscribed emails.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    emails = Newsletter.objects.all()

    context = {
        'title': 'RetroTech Newsletter Emails',
        'emails': emails,
    }

    return render(request, 'home/newsletter-emails.html', context)


@login_required
def delete_newsletter_email(request, email_id):
    """
    Deleting newsletter emails if subscribed person wants to.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    email = get_object_or_404(Newsletter, pk=email_id)
    email.delete()
    messages.success(request, f'{ email.news_email } \
                      has was successfully removed.')
    return redirect('newsletter-emails')


@login_required
def sell_to_me(request):
    """
    Rendering messages send to me to sell items.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    sells = SellToUs.objects.all()

    context = {
        'title': 'RetroTech Sell to me!?',
        'sells': sells,
    }

    return render(request, 'home/sell-to-me.html', context)


@login_required
def sell_to_me_details(request, sell_id):
    """
    Takes sell to us id and renders as detailed query sent to me.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    sell = get_object_or_404(SellToUs, pk=sell_id)

    context = {
        'title': 'RetroTech Sell to me details',
        'sell': sell,
    }

    return render(request, 'home/sell-to-me-details.html', context)


@login_required
def admin_orders(request):
    """
    Preview of orders made on website.
    """
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))

    orders = Order.objects.all()

    context = {
        'title': 'RetroTech Orders',
        'orders': orders,
    }

    return render(request, 'home/orders.html', context)


@login_required
def admin_orders_preview(request, order_id):
    """
    Preview of selected orders.
    """
    items = Item.objects.all()
    order = get_object_or_404(Order, pk=order_id)

    context = {
        'title': 'RetroTech Order preview',
        'order': order,
        'items': items,
    }

    return render(request, 'home/admin-orders-preview.html', context)
