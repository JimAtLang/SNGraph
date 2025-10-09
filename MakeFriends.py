from datetime import datetime
from random import choice
from typing import List

from DateGenerator import random_date
from User import User


def make_friends(users: List[User], num_users: int, start_date:datetime) -> List[str]:
    friendings = []
    for i in range(50):
        user1: User = choice(users)
        user2: User = user1
        while user2 == user1 or user2 in user1.edges:
            user2 = choice(users)
        dt = random_date(start_date, datetime.now())
        user1.add_edge(user2)
        friendings.append(f"{user1.name} added {user2.name} as a friend on {dt:%B %d, %Y}\n")
    return friendings