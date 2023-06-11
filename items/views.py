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
