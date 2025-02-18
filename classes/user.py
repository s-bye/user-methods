class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.__password = password
        self.birthday = birthday

    def get_details(self):
        return f'User ID: {self.user_id}\nName: {self.name}\nSurname: {self.surname}\nEmail: {self.email}\nBirthday: {self.birthday}'
    
    def get_age(self):
        return 2025 - int(self.birthday[-4:])