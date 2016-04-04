# Standard libs
from collections import OrderedDict

# Mock user collection
# Maps username to User object. Only stores data in memory, so it won't persist
# anything when the app exits. I'm using an OrderedDict so that users will be
# listed in the order in which they're created.
USER_COLLECTION = OrderedDict()

class User(object):
    @classmethod
    def create(cls, username, email, password_hash):
        # Create a user and store them in the mock collection
        user = User(username, email, password_hash)
        USER_COLLECTION[username] = user
        return user

    @classmethod
    def get_by_username(cls, username):
        # Retrieve a user by their username
        return USER_COLLECTION.get(username, None)

    @classmethod
    def get_all(cls):
        # Retrieve all users
        return USER_COLLECTION.values()

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

