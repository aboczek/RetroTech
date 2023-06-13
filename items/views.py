from django.shortcuts import render


def handheld(request):
    """
    Handheld devices page.
    """

    context = {
        'title': 'RetroTech Handhelds',
    }

    return render(request, 'items/handheld.html', context)


def console(request):
    """
    Console devices page.
    """

    context = {
        'title': 'RetroTech Consoles',
    }

    return render(request, 'items/console.html', context)


def accessory(request):
    """
    Accessories page.
    """

    context = {
        'title': 'RetroTech Accessories',
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
