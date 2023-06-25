from django.shortcuts import render, get_object_or_404
from items.models import Category, Item


def handheld(request):
    """
    Handheld devices page.
    """

    items = Item.objects.all()
    context = {
        'title': 'RetroTech Handhelds',
        'items': items,
    }

    return render(request, 'items/handheld.html', context)


def console(request):
    """
    Console devices page.
    """

    items = Item.objects.all()
    context = {
        'title': 'RetroTech Consoles',
        'items': items,
    }

    return render(request, 'items/console.html', context)


def accessory(request):
    """
    Accessories page.
    """

    items = Item.objects.all()
    context = {
        'title': 'RetroTech Accessories',
        'items': items,
    }

    return render(request, 'items/accessory.html', context)


def games(request):
    """
    Games page.
    """

    context = {
        'title': 'RetroTech Games coming soon',
    }

    return render(request, 'items/games.html', context)


def sell_to_us(request):
    """
    Sell to us page with steps how to do it.
    """

    context = {
        'title': 'RetroTech Sell to us',
    }

    return render(request, 'items/sell-to-us.html', context)


def sale(request):
    """
    Sale page.
    """

    items = Item.objects.all()
    context = {
        'title': 'RetroTech SALE!!',
        'items': items,
    }

    return render(request, 'items/sale.html', context)


def item_detail(request, item_id):
    """
    Item details to render individual items.
    """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'title': 'RetroTech {{ Item.name}}',
        'item': item,
    }

    return render(request, 'items/item-detail.html', context)
