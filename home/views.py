from django.shortcuts import render


def home(request):
    """
    Home page
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
