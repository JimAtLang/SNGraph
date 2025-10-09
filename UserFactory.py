from typing import List
from User import User
from NameGenerator import get_name


def get_users(number:int):
    users: List[User] = []
    used_names: List[str] = [""]
    for i in range(number):
        name: str = ""
        while name in used_names:
            name = get_name()
        used_names.append(name)
        user: User = User(get_name())
        users.append(user)
    return users