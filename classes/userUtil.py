import random
import datetime as dt
import string as st

class UserUtil:
    @staticmethod
    def generate_user_id():
        current_year = dt.datetime.now().year % 100
        random_number = random.randint(100000, 999999)
        return f'{current_year:02d}{random_number:06d}'

    @staticmethod
    def generate_password():
        password = [
        random.choice(st.ascii_lowercase),
        random.choice(st.ascii_uppercase),
        random.choice(st.digits),
        random.choice(st.punctuation)
        ]
        password += random.choices(st.ascii_letters + st.digits + st.punctuation, k=4)
        return ''.join(password)


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
        if '@' not in email and '.' not in email:
            return False

        parts = email.split('@')

        if len(parts) != 2:
            return False

        local, domain = parts

        if not local:
            return False
        if not '.' in domain:
            return False

        domain_parts = domain.split('.')

        if len(domain_parts) < 2:
            return False
        return True