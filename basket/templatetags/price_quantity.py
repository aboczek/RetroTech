from django import template


register = template.Library()


@register.filter(name='calculator')
def calculator(price, quantity):
    """
    Calculates total price per item * quantity of it.
    """
    return price * quantity
