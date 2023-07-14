from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from home.forms import NewsletterForm
from home.models import Newsletter


def newsletter(request):
    """
    Context processor for newsletter.
    """
    newsletter_form = NewsletterForm()

    # if request.method == 'POST':
    if 'news_email' in request.POST and request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            if Newsletter.objects.filter(news_email=instance.news_email).exists():
                messages.error(request, f'{instance.news_email} is \
                                already subscribed!')
            else:
                instance.save()
                cust_email = instance.news_email
                subject = render_to_string(
                    'newsletter_emails/newsletter_email_subject.txt',
                    {'instace': instance})
                body = render_to_string(
                    'newsletter_emails/newsletter_email_body.txt',
                    {'instace': instance,
                     'contact_email': settings.DEFAULT_FROM_EMAIL})

                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [cust_email]
                )
                messages.success(request, f'{instance.news_email} has \
                                  subscribed for newsletter!')

    else:
        newsletter_form = NewsletterForm()

    context = {
                'newsletter_form': newsletter_form,
            }
    return context
