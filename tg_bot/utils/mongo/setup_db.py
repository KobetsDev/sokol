from pymongo import MongoClient
from .cred import username, password, client_str
# username = input()
# password = input()

client = MongoClient(client_str)
# setup db
# db_name = 'sokol_bot'
db_name = 'tg_bot'
db = client[db_name]
# setup user collection
col_users_name = 'users'
collection_users = db[col_users_name]

# stup products collection
col_products_name = 'products'
collection_products = db[col_products_name]

# stup cart collection
col_cart_name = 'cart'
collection_cart = db[col_cart_name]

# setup admin collection
col_admins_name = "admins"
collection_admins = db[col_admins_name]

# setup doors collection
col_orders = 'doors'
collection_door = db[col_orders]

# setup orders collection
col_orders = 'orders'
collection_door = db[col_orders]
