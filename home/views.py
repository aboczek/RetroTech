from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from items.models import Category, Item
from .forms import ItemsForm
import cloudinary.uploader


def home(request):
    """
    Home page.
    """
    context = {
        'title': 'RetroTech Home Page',
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

    context = {
        'title': 'RetroTech User Account',
    }

    return render(request, 'home/profile.html', context)


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
