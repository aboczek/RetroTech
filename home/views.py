from django.shortcuts import render


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
    Track your order page to see tracking.
    """

    context = {
        'title': 'RetroTech User Account'
    }

    return render(request, 'home/profile.html', context)
