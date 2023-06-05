from models.user import User
from repositories.RepositoryInterface import RepositoryInterface


class RepositoryImpl(RepositoryInterface):
    def __init__(self):
        self._users = []

    def sign_up(self, user: User):
        self._users.append(user)

    def login(self, user_id):
        for i in range(len(self._users)):
            if self._users[i].get_id == user_id:
                return self._users[i]
