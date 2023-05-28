from django.shortcuts import render


def home(request):
    """
    Home page
    """
    context = {
        'title': 'RetroTech Home Page',
    }

    return render(request, 'home/index.html', context)
