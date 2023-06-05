
class User:
    def __init__(self, name, student_id):
        self._name = name
        self._user_id = student_id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_user_id(self, user_id):
        self._user_id = user_id

    def get_user_id(self):
        return self._user_id

    def download_resources(self):
        pass

