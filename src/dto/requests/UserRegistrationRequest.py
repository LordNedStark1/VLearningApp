class UserRegistrationRequest:
    user_type = ""

    def get_name(self):
        pass

    def get_user_type(self):
        return self.user_type

    def set_user_type(self, user_type):
        self.user_type = user_type
