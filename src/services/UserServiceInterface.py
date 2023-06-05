from abc import ABC, abstractmethod
from dto.requests.UserRegistrationRequest import UserRegistrationRequest
from dto.requests.UserLoginRequest import UserLoginRequest


class UserServiceInterface(ABC):
    @abstractmethod
    def sign_up(self, user_reg_request: UserRegistrationRequest):
        pass

    @abstractmethod
    def login(self, user_login_request: UserLoginRequest):
        pass

    @abstractmethod
    def view_membership_strength(self):
        pass
