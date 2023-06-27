from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from items.models import Item, Category


def all_items(request):
    """
    Handheld devices page.
    """

    items = Item.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('all_items'))

            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            items = items.filter(queries)

    context = {
        'title': 'RetroTech Handhelds',
        'items': items,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'items/all-items.html', context)


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
