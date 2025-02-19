# User Management System 

This project is a simple user management system implemented in Python. It allows you to create, update, delete, and manage users. The project includes utility functions for generating user IDs, passwords, and validating emails.

## Project Structure 📂

- `classes/user.py`: Contains the `User` class which represents a user.
- `classes/userService.py`: Contains the `UserService` class which manages user operations.
- `classes/userUtil.py`: Contains the `UserUtil` class which provides utility functions for user management.
- `main.py`: The main script to demonstrate the functionality of the user management system.

## What I learned 📚

- **Utility Functions**: I learned how to create utility functions to generate user IDs, passwords, and validate emails.
- **Object-Oriented Programming**: I learned how to create classes and objects to represent users and user services.
- **User Management**: I learned how to create, update, delete, and manage users in a user management system.
- **Email and password validation**: I learned how to validate email addresses and passwords using regular expressions.
- **Unit Testing**: I learned how to write unit tests to test the functionality of the user management system.

## Instructions to Run the Code 🏃‍♂️

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

### Input:
```python
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
```

### Output:
```python
User ID: 2501234567
Name: Andrey
Surname: Tkachev
Email: andrey.tkachev@gmail.com
Birthday: 05-05-2002

User ID: 2502345678
Name: Erik
Surname: Akimov
Email: erik.akimov@gmail.com
Birthday: 18-02-2005

User ID: 2503456789
Name: Elza
Surname: Rakhmanova
Email: elza.rakhmanova@gmail.com
Birthday: 13-07-1999

User ID: 2504567890
Name: Vladimir
Surname: Petrov
Email: vladimir.petrov@gmail.com
Birthday: 25-12-2000
```

# UML Diagram 🖼️
![UML Diagram](https://i.ibb.co/mFyLNCcD/UML-1.jpg)