from django import forms
from items.models import Item
from .models import Newsletter
from checkout.models import UserProfile


class ItemsForm(forms.ModelForm):
    """
    Items model.
    """
    class Meta:
        """
        Random docstring.
        """

        model = Item
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    """
    Form for orders.
    """
    class Meta:
        """
        Meta for OrderForm.
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholder and classes,
        remove auto-generated labels,
        and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county_state': 'County or State',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class NewsletterForm(forms.ModelForm):
    """
    Takes emails for newsletter subscribers.
    """
    class Meta:
        """
        Meta for NewsletterForm
        """
        model = Newsletter
        fields = ('news_email',)
