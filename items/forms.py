from django import forms
from .models import SellToUs


class SellToUsForm(forms.ModelForm):
    """
    Sell to us model form.
    """
    class Meta:
        """
        Meta for Sell to us.
        """
        model = SellToUs
        fields = (
            'full_name', 'email', 'brand',
            'model', 'grade', 'description',
            'sell_image_one', 'sell_image_two',
            'sell_image_three',
        )

        labels = {
            'grade': 'Grade - Like new, lightly scratched or used',
            'sell_image_one': 'Image one',
            'sell_image_two': 'Image two',
            'sell_image_three': 'Image three',
        }
