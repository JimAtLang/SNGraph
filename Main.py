from datetime import datetime
from DateGenerator import random_date
from NameGenerator import get_name
from User import User
from typing import List, Dict, TextIO
from random import randint, choice
from PostGenerator import get_posts

f: TextIO

start_date:datetime = datetime(2020, 1, 1)
print(random_date(start_date, datetime.now()))

users:List[User] = []
used_names:List[str] = [""]
for i in range(10):
    name:str = ""
    while name in used_names:
        name = get_name()
    used_names.append(name)
    user:User = User(get_name())
    users.append(user)
with open("log.txt", "w") as f:
    for i in range(50):
        user1: User = choice(users)
        user2: User = user1
        while user2 == user1 or user2 in user1.edges:
            user2 = choice(users)
        dt = random_date(start_date, datetime.now())
        user1.add_edge(user2)
        f.write(f"{user1.name} added {user2.name} as a friend on {dt:%B %d, %Y}\n")

with open("posts.txt", "w") as f:
    f.writelines(get_posts(users, 200))

#TODO: make a BFS traverser with a set range
#TODO: come up with a secret algorithm for friends of friends posts
#TODO: make a like generator using BFS traverser based on popularity of posts
#TODO: generate friending, posts, and likes as lists then write them all out randomly