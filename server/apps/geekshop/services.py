from random import choice as random_choice

from server.apps.geekshop.models import Product


def get_promotion_product():
    return random_choice(Product.objects.filter(is_active=True))
