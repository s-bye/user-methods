class UserService:
    users = {}

    def add_user(cls, user):
        cls.users[user.user_id] = user
        return cls.users

    def find_user(cls, user_id):
        return cls.users.get(user_id)

    def delete_user(cls, user_id):
        return cls.users.pop(user_id)

    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            user = cls.users[user_id]
            user.name = user_update.name
            user.surname = user_update.surname
            user.email = user_update.email
            user.__password = user_update.__password
            user.birthday = user_update.birthday

    def get_number(cls):
        return len(cls.users)