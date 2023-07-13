from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.db.models.functions import Lower
from items.models import Item, Category, SellToUs
from .forms import SellToUsForm


def all_items(request):
    """
    Handheld devices page.
    """

    items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('product_name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria! \
                                  You are viewing all products.")
                return redirect(reverse('all_items'))

            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            items = items.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'title': 'RetroTech Handhelds',
        'items': items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
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
    sell_form = SellToUsForm()
    if request.method == 'POST':
        sell_form = SellToUsForm(request.POST, request.FILES)
        if sell_form.is_valid():
            instance = sell_form.save()
            instance.save()
            cust_email = instance.email
            subject = render_to_string(
                'sell_to_us_emails/sell_to_us_subject.txt',
                {'instance': instance})
            body = render_to_string(
                'sell_to_us_emails/sell_to_us_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )
            messages.success(request, 'Query has been accepted, \
                              please wait for our response.')
            return redirect('sell_to_us')

    else:
        sell_form = SellToUsForm()

    context = {
        'title': 'RetroTech Sell to us',
        'sell_form': sell_form,
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
        'title': 'RetroTech',
        'item': item,
    }

    return render(request, 'items/item-detail.html', context)
