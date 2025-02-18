import random
import datetime as dt

class UserUtil:
    @staticmethod
    def generate_user_id():
        current_year = dt.datetime.now().year % 100
        random_number = random.randint(100000, 999999)
        return f'{current_year:02d}{random_number:06d}'

    @staticmethod
    def generate_password():
        return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=?/';:>.<,~`", k=8))

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8 and not any(char.isdigit() for char in password) and not any(char.isupper() for char in password) and not any(char.islower() for char in password):
            return False
        return True

    @staticmethod
    def generate_email(name, surname, domain):
        return f'{name.lower()}.{surname.lower()}@{domain}'

    @staticmethod
    def validate_email(email):
        if '@' in email:
            return True


