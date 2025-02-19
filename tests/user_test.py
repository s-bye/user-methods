import unittest
from classes.user import User

class TestUser(unittest.TestCase):

    def user_details_are_correct(self):
        user = User(1, "John", "Doe", "john.doe@example.com", "password123", "01-01-2000")
        expected_details = "User ID: 1\nName: John\nSurname: Doe\nEmail: john.doe@example.com\nBirthday: 01-01-2000"
        self.assertEqual(user.get_details(), expected_details)

    def user_age_is_correct(self):
        user = User(1, "John", "Doe", "john.doe@example.com", "password123", "01-01-2000")
        self.assertEqual(user.get_age(), 25)

    def user_age_with_future_birthday(self):
        user = User(1, "John", "Doe", "john.doe@example.com", "password123", "01-01-2026")
        self.assertEqual(user.get_age(), -1)

    def user_age_with_invalid_birthday_format(self):
        user = User(1, "John", "Doe", "john.doe@example.com", "password123", "2000-01-01")
        with self.assertRaises(ValueError):
            user.get_age()

if __name__ == '__main__':
    unittest.main()