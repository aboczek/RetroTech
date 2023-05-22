from django.db import models


class Category(models.Model):
    """
    Creates Categories to let the user use search bar.
    """
    name = models.CharField(max_length=254)
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
                                 blank=True, on_delete=models.SET_NULL)
    sku_number = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=256)
    product_model = models.CharField(max_length=254, null=True, blank=True)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.BooleanField()
    feature = models.BooleanField()

    def __str__(self):
        return str(self.product_name)


class Image(models.Model):
    """
    Uploading multiply images to Item.
    """
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
