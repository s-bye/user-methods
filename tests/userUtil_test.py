import unittest
import string as st
from classes.userUtil import UserUtil

class TestUserUtil(unittest.TestCase):

    def generate_user_id_creates_valid_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertEqual(len(user_id), 8)
        self.assertTrue(user_id[:2].isdigit())
        self.assertTrue(user_id[2:].isdigit())

    def generate_password_creates_valid_password(self):
        password = UserUtil.generate_password()
        self.assertEqual(len(password), 8)
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in st.punctuation for char in password))

    def is_strong_password_returns_true_for_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password('Aa1!aaaa'))

    def is_strong_password_returns_false_for_weak_password(self):
        self.assertFalse(UserUtil.is_strong_password('weak'))

    def generate_email_creates_valid_email(self):
        email = UserUtil.generate_email('John', 'Doe', 'example.com')
        self.assertEqual(email, 'john.doe@example.com')

    def validate_email_returns_true_for_valid_email(self):
        self.assertTrue(UserUtil.validate_email('john.doe@example.com'))

    def validate_email_returns_false_for_invalid_email(self):
        self.assertFalse(UserUtil.validate_email('john.doe@com'))
        self.assertFalse(UserUtil.validate_email('john.doeexample.com'))
        self.assertFalse(UserUtil.validate_email('john.doe@.com'))
        self.assertFalse(UserUtil.validate_email('@example.com'))