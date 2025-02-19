from classes.user import User
from classes.userUtil import UserUtil
from classes.userService import UserService

if __name__ == '__main__':
    user1 = User(UserUtil.generate_user_id(), 'Andrey', 'Tkachev', UserUtil.generate_email('Andrey', 'Tkachev','gmail.com'), UserUtil.generate_password(), '05-05-2002')
    user2 = User(UserUtil.generate_user_id(), 'Erik', 'Akimov', UserUtil.generate_email('Erik', 'Akimov', 'gmail.com'), UserUtil.generate_password(), '18-02-2005')
    user3 = User(UserUtil.generate_user_id(), 'Elza', 'Rakhmanova', UserUtil.generate_email('Elza', 'Rakhmanova', 'gmail.com'), UserUtil.generate_password(), '13-07-1999')
    user4 = User(UserUtil.generate_user_id(), 'Vladimir', 'Petrov', UserUtil.generate_email('Vladimir', 'Petrov', 'gmail.com'), UserUtil.generate_password(), '25-12-2000')

    UserService().add_user(user1)
    UserService().add_user(user2)
    UserService().add_user(user3)
    UserService().add_user(user4)

    for user in UserService.users.values():
        print(user.get_details())
        print()