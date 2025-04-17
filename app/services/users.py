from app.modules.users import user

def create_user(user_data):
    new_user = user.user_to_json(user_data)
    return new_user

def store_user(user):
