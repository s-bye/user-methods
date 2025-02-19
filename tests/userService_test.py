import unittest
from unittest.mock import patch
from classes.userService import UserService

class UserServiceTest(unittest.TestCase):

    @patch('userService.UserRepository')
    def user_creation_successful(self, MockUserRepository):
        user_service = UserService(MockUserRepository)
        result = user_service.create_user('John', 'Doe', 'john.doe@example.com')
        self.assertTrue(result)

    @patch('userService.UserRepository')
    def user_creation_fails_with_invalid_email(self, MockUserRepository):
        user_service = UserService(MockUserRepository)
        result = user_service.create_user('John', 'Doe', 'invalid-email')
        self.assertFalse(result)

    @patch('userService.UserRepository')
    def user_creation_fails_with_missing_first_name(self, MockUserRepository):
        user_service = UserService(MockUserRepository)
        result = user_service.create_user('', 'Doe', 'john.doe@example.com')
        self.assertFalse(result)

    @patch('userService.UserRepository')
    def user_creation_fails_with_missing_last_name(self, MockUserRepository):
        user_service = UserService(MockUserRepository)
        result = user_service.create_user('John', '', 'john.doe@example.com')
        self.assertFalse(result)

    @patch('userService.UserRepository')
    def user_creation_fails_with_duplicate_email(self, MockUserRepository):
        MockUserRepository.find_by_email.return_value = True
        user_service = UserService(MockUserRepository)
        result = user_service.create_user('John', 'Doe', 'john.doe@example.com')
        self.assertFalse(result)