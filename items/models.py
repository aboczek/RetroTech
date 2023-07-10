from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Creates Categories to let the user use search bar.
    """

    class Meta:
        """
        Fixing bug in admin that would render category as categorys.
        """
        verbose_name_plural = 'Categories'

    CATEGORY_CHOICES = {
        ('handheld', 'Handheld'),
        ('console', 'Console'),
        ('accessories', 'Accessories'),
        ('games', 'Games'),
    }

    name = models.CharField(max_length=254, choices=CATEGORY_CHOICES)
    frontend_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_frontend_name(self):
        """
        Returns frontend name.
        """
        return self.frontend_name


class Item(models.Model):
    """
    Item database model.
    """
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.CASCADE)
    sku_number = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254, null=False, blank=False)
    product_model = models.CharField(max_length=254, null=True, blank=True)
    product_description = models.TextField()
    quantity = models.PositiveBigIntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                null=False, blank=False)
    sale = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    image_one = CloudinaryField(null=True, blank=True, default='placeholder')
    image_two = CloudinaryField(null=True, blank=True, default='placeholder')
    image_three = CloudinaryField(null=True, blank=True, default='placeholder')

    def __str__(self):
        return str(self.product_name)
