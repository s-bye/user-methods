import unittest
from classes.user import User
from classes.userUtil import UserUtil
from classes.userService import UserService

class TestUserService(unittest.TestCase):

    def adds_users_correctly(self):
        user1 = User(UserUtil.generate_user_id(), 'Andrey', 'Tkachev', UserUtil.generate_email('Andrey', 'Tkachev','gmail.com'), UserUtil.generate_password(), '05-05-2002')
        user2 = User(UserUtil.generate_user_id(), 'Erik', 'Akimov', UserUtil.generate_email('Erik', 'Akimov', 'gmail.com'), UserUtil.generate_password(), '18-02-2005')
        user3 = User(UserUtil.generate_user_id(), 'Elza', 'Rakhmanova', UserUtil.generate_email('Elza', 'Rakhmanova', 'gmail.com'), UserUtil.generate_password(), '13-07-1999')
        user4 = User(UserUtil.generate_user_id(), 'Vladimir', 'Petrov', UserUtil.generate_email('Vladimir', 'Petrov', 'gmail.com'), UserUtil.generate_password(), '25-12-2000')

        service = UserService()
        service.add_user(user1)
        service.add_user(user2)
        service.add_user(user3)
        service.add_user(user4)

        self.assertEqual(len(service.users), 4)
        self.assertIn(user1.user_id, service.users)
        self.assertIn(user2.user_id, service.users)
        self.assertIn(user3.user_id, service.users)
        self.assertIn(user4.user_id, service.users)

    def duplicate_user_ids(self):
        user_id = UserUtil.generate_user_id()
        user1 = User(user_id, 'Andrey', 'Tkachev', UserUtil.generate_email('Andrey', 'Tkachev','gmail.com'), UserUtil.generate_password(), '05-05-2002')
        user2 = User(user_id, 'Erik', 'Akimov', UserUtil.generate_email('Erik', 'Akimov', 'gmail.com'), UserUtil.generate_password(), '18-02-2005')

        service = UserService()
        service.add_user(user1)
        with self.assertRaises(ValueError):
            service.add_user(user2)

    def retrieves_user_details(self):
        user = User(UserUtil.generate_user_id(), 'Andrey', 'Tkachev', UserUtil.generate_email('Andrey', 'Tkachev','gmail.com'), UserUtil.generate_password(), '05-05-2002')
        service = UserService()
        service.add_user(user)

        details = service.users[user.user_id].get_details()
        self.assertIn('Andrey', details)
        self.assertIn('Tkachev', details)
        self.assertIn('gmail.com', details)

if __name__ == '__main__':
    unittest.main()