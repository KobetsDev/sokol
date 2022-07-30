from dataclasses import dataclass
import random
import time
from datetime import datetime, timedelta
import pytz
import asyncio

from pymongo.errors import DuplicateKeyError
from setup_db import collection_cart
# from setup_db

from products_class import Products


class Cart:

    def add_product_in_cart(self, product: dict):
        product_to_add = {
            'user_id': product.get('user_id'),
            'products': product.get('products'),
            'date_order': int(time.time())
        }
        try:
            collection_cart.insert_one(product_to_add)
            return True
        except DuplicateKeyError:
            print(f"Duplicate Error: {product.get('_id')}")
            return False

    @staticmethod
    def get_info(user_id: int):
        return collection_cart.find_one({'user_id': user_id})


# PD = Products()
# products_mass = [PD.get_info(12345), PD.get_info(12346)]
# C = Cart()
# C.add_product_in_cart({
#     'user_id': 55555,
#     'products': [
#         {
#             'product_id': product.get('_id'),
#             'product_count': random.randrange(1, 10)
#         }
#         for product in products_mass
#     ],
#     'date_order': '2020.11.22',
# })
# f = C.get_info(
#     user_id=55555
# )
# print(f)
