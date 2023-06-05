from dto.requests.UserLoginRequest import UserLoginRequest
from dto.requests.UserRegistrationRequest import UserRegistrationRequest
from models.student import Student
from repositories.RepositoryImpl import RepositoryImpl
from services.UserServiceInterface import UserServiceInterface

repo = RepositoryImpl()


def sign_up_admin(user_reg_request: UserRegistrationRequest):
    pass


class UserServiceImpl(UserServiceInterface):

    def __init__(self):
        self.counter = 0

    def login(self, user_login_request: UserLoginRequest):
        pass

    def sign_up(self, user_reg_request: UserRegistrationRequest):

        user_type = user_reg_request.get_user_type()

        if user_type == "student":
            self.sign_up_student(user_reg_request)
        elif user_type == "admin":
            sign_up_admin(user_reg_request)
        else:
            return "invalid user sign_up"
        return 'sign up successful'

    def sign_up_student(self, user_reg_request: UserRegistrationRequest):
        student = Student(user_reg_request.get_name(), self.generate_user_id())
        repo.sign_up(student)

    def view_membership_strength(self):
        return

    def generate_user_id(self):
        self.counter += 1
        return self.counter
