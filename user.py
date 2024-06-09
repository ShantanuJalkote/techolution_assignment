
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def get_name(self):
        return self.name

    def get_user_id(self):
        return self.user_id

    def __repr__(self):
        return f"User(name={self.get_name()}, user_id={self.get_user_id()})"
