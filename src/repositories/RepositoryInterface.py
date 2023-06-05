from abc import ABC,abstractmethod

from models.user import User


class RepositoryInterface (ABC):

    @abstractmethod
    def sign_up(self, user : User):
        pass


    @abstractmethod
    def login(self, user_id):
        pass