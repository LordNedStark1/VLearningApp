from unittest import TestCase

from dto.requests.UserRegistrationRequest import UserRegistrationRequest
from services.UserServiceImpl import UserServiceImpl


class VLATest(TestCase):
    user_service = UserServiceImpl()
    user_reg_req = UserRegistrationRequest()
    user_reg_req2 = UserRegistrationRequest()
    user_reg_req.set_user_type("student")
    user_reg_req2.set_user_type("admin")

    def test_user_can_sign_up(self):

       response = self.user_service.sign_up(self.user_reg_req)

       self.assertEqual('sign up successful', response)
       strength = self.user_service.view_membership_strength()
       self.assertEqual(1, strength)

    def test_two_user_sign_up(self):
        self.user_service.sign_up(self.user_reg_req)
        self.user_service.sign_up(self.user_reg_req2)

        strength = self.user_service.view_membership_strength()
        self.assertEqual(2, strength)
