from datetime import datetime
from DateGenerator import random_date
from NameGenerator import get_name
from User import User
from typing import List, Dict
from random import randint, choice

start_date:datetime = datetime(2020, 1, 1)
print(random_date(start_date, datetime.now()))

users:List[User] = []
used_names:List[str] = [""]
for i in range(10):
    name:str = ""
    while name in used_names:
        name = get_name()
    used_names.append(name)
    user:User = User(get_name().split()[0])
    users.append(user)

for i in range(50):
    user1: User = choice(users)
    user2: User = user1
    while user2 == user1 or user2 in user1.edges:
        user2 = choice(users)
    dt = random_date(start_date, datetime.now())
    #TODO: make some kind of list of friend/unfriend events & add to list
    # or just add the friend and list the friending/unfriending in a text file