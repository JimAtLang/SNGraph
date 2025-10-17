from datetime import datetime
from DateGenerator import random_date
from User import User
from typing import List, Dict, TextIO
from random import randint, choice
from PostGenerator import get_posts
from UserFactory import get_users
from MakeFriends import make_friends
from LikeGenerator import make_likes


f: TextIO

start_date:datetime = datetime(2020, 1, 1)
print(random_date(start_date, datetime.now()))

users:List[User] = get_users(10)
friendings:List[str] = make_friends(users, 50, start_date=start_date)
for friend in friendings:
    print(friend)

posts = get_posts(users, 200)
for post in posts:
    print(post)

likings = make_likes(users, 200)
for liking in likings:
    print(liking)

with open("log.txt", "w") as f:
    friends_recorded = 0
    posts_recorded = 0
    likes_recorded = 0
    #FIXME: this isn't recording everything
    while likes_recorded < len(likings) and posts_recorded < len(posts) and friends_recorded < len(friendings):
        n = randint(0,2)
        if n == 0:
            f.write(likings[likes_recorded])
            likes_recorded += 1
        elif n == 1:
            f.write(posts[posts_recorded])
            posts_recorded += 1
        else:
            f.write(friendings[friends_recorded])
            friends_recorded += 1



