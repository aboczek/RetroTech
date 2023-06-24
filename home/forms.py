from django import forms
from items.models import Category, Item


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
