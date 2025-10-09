from datetime import datetime
from DateGenerator import random_date
from User import User
from typing import List, Dict, TextIO
from random import randint, choice
from PostGenerator import get_posts
from UserFactory import get_users
from MakeFriends import make_friends

f: TextIO

start_date:datetime = datetime(2020, 1, 1)
print(random_date(start_date, datetime.now()))

users:List[User] = get_users(10)
friendings:List[str] = make_friends(users, 50, start_date=start_date)

with open("log.txt", "w") as f:
    f.writelines(get_posts(users, 200))

#TODO: make a BFS traverser with a set range
#TODO: come up with a secret algorithm for friends of friends posts
#TODO: generate friending, posts, and likes as lists then write them all out randomly