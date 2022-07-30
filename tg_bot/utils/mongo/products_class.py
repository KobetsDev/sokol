from dataclasses import dataclass
import time
from datetime import datetime, timedelta
import pytz
import asyncio

from pymongo.errors import DuplicateKeyError
from setup_db import collection_products
# from setup_db


class Products:

    def add_product(self, product: dict):
        product_to_add = {
            '_id': product.get('product_id'),  # telegram id,
            'title': product.get('title'),
            'description': product.get('description'),
            'image_url': product.get('image_url'),
            'price': product.get('price'),
        }
        try:
            collection_products.insert_one(product_to_add)
            return True
        except DuplicateKeyError:
            print(f"Duplicate Error: {product.get('_id')}")
            return False

    @staticmethod
    def get_info(product_id: int):
        return collection_products.find_one({'_id': product_id})

#
# PD = Products()
# PD.add_product({
#     'product_id': 12346,
#     'title': 'Чупа-Чупс',
#     'description': 'Сасный.',
#     'image_url': 'http://image.com/',
#     'price': 40_00,
#     'date_order': '2020.11.12',
# })
# f = PD.get_info(
#     product_id=12345
# )
# print(f)
