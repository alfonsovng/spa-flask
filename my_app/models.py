from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, email):
        self._email = email
        self._password = "123" #TODO: get a real password from someplace

    def get_id(self):
        return self._email
    
    @property
    def email(self):
    	return self._email

    def check_password(self, password):
        return self._password == password
    
    @staticmethod
    def find_user(email):
        return User(email = email)
    