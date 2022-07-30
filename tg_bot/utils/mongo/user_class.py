import time
# from datetime import datetime, timedelta
# import pytz
# import asyncio

from pymongo.errors import DuplicateKeyError
from .setup_db import collection_users, collection_admins, collection_door


class User:
    """
    User class
    """
    user_status = {
        "started": 0,
        "registered": 1,
        "banned": 2,
    }

    def __init__(self, user_id):
        self.user_id = user_id

    def add_user(self, user: dict, message: str):
        user_to_add = {
            '_id': self.user_id,  # telegram id,
            'first_name': user.get('first_name'),
            'last_name': user.get('last_name'),
            'username': user.get('username'),
            'is_admin': False,
            'date_registered': int(time.time()),
            'date_last_active': int(time.time()),
            'status': self.user_status["started"],  # started,skipped, registered, banned
            'add_last_sent': None,
            'activity': [
                {
                    'text': message,
                    'timestamp': int(time.time()),
                },
            ],
        }
        try:
            collection_users.insert_one(user_to_add)
            return True
        except DuplicateKeyError:
            print(f"Duplicate Error: {self.user_id}")
            return False

    def get_info(self):
        return collection_users.find_one({'_id': self.user_id})

    async def register_user(self, phone_number):
        # add try except
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    'phone_number': phone_number
                }
            }
        )
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    'status': self.user_status["registered"]
                }
            }
        )


    def update_last_active(self):
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    "date_last_active": int(time.time())
                }
            }
        )
        print("update successful for", self.user_id)

    def update_activity_list(self, message: str):
        pass

    def update_field(self, field, value):
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    field: value
                }
            }
        )

    async def activate_door(self):
        # add try except
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    'door.active': True
                }
            }
        )
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    'status': self.user_status["registered"]
                }
            }
        )

    async def deactivate_door(self):
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    'door.active': False
                }
            }
        )
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    'status': False
                }
            }
        )
    async def change_user_status(self): # to be changed
        collection_users.update_one(
            {

                '_id': self.user_id
            },
            {
                '$set': {
                    'door.active': False
                }
            }
        )
        collection_users.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    'status': False
                }
            }
        )
