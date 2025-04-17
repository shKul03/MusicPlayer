from app.config import config

class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_to_json(self):
        json_user = {
            "username" : self.username,
            "password" : self.password
        }
        return json_user