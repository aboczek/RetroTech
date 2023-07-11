from django.shortcuts import get_object_or_404
from django.contrib import messages
from home.forms import NewsletterForm
from home.models import Newsletter


def newsletter(request):
    """
    Context processor for newsletter.
    """
    newsletter_form = NewsletterForm()
    newsletters = Newsletter.objects.all()
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            if Newsletter.objects.filter(email=instance.email).exists():
                messages.error(request, f'{instance.email} is \
                                already subscribed!')
            else:
                instance.save()
                messages.success(request, f'{instance.email} has \
                                  subscribed for newsletter!')

    else:
        newsletter_form = NewsletterForm()

    context = {
                'newsletter_form': newsletter_form,
            }
    return context
