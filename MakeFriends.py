from datetime import datetime
from random import choice
from typing import List

from DateGenerator import random_date
from User import User

def make_friend(users: List[User], start_date:datetime) -> str:
    user1: User = choice(users)
    user2: User = user1
    while user2 == user1 or user2 in user1.edges:
        user2 = choice(users)
    user1.add_edge(user2)
    return f"{user1.name} added {user2.name} as a friend on {start_date:%B %d, %Y}\n"


def make_friends(users: List[User], num_users: int, start_date:datetime) -> List[str]:
    friendings = []
    for i in range(num_users):
        user1:User = User("none")
        while user1.name == "none" or len(user1.edges) == len(users):
            user1 = choice(users)
        user2: User = user1
        while user2 == user1 or user2 in user1.edges:
            user2 = choice(users)
        dt = start_date
        user1.add_edge(user2)
        friendings.append(f"{user1.name} added {user2.name} as a friend on {dt:%B %d, %Y}\n")
    return friendings