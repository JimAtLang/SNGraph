from datetime import datetime, timedelta
from DateGenerator import random_date
from User import User
from typing import List, Dict, TextIO
from random import shuffle, randint
from PostGenerator import get_posts, get_post
from UserFactory import get_users
from MakeFriends import make_friends, make_friend
from LikeGenerator import make_likes, make_like, make_repost


f: TextIO

start_date:datetime = datetime(2020, 1, 1)




with open("log2.txt", "w") as f:
    users: List[User] = get_users(12)
    posts = get_posts(users, 50)
    likings = []
    f.writelines(likings)
    friendings = []
    reposts = []
    while start_date < datetime.now():
        year = start_date.year
        if year == 2020:
            n = randint(1,6)
        else:
            n = randint(1, 20)
        if n == 1:
            friending = make_friend(users,start_date)
            print(friending)
            f.write(friending)
            friendings.append(friending)
        elif 2 <= n <= 6:
            post = get_post(users,start_date)
            print(post)
            f.write(post)
            posts.append(post)
        elif 7 <= n <= 10:
            repost = make_repost(users,start_date)
            print(repost)
            f.write(repost)
            reposts.append(repost)
        else:
            like =make_like(users,start_date)
            print(like)
            f.write(like)
            likings.append(like)
        dt = randint(1,5)
        start_date += timedelta(days=dt)


# friendings:List[str] = make_friends(users, 50, start_date=start_date)
# # for friend in friendings:
# #     print(friend)
#
# posts = get_posts(users, 200)
# # for post in posts:
# #     print(post)
#
# likings = make_likes(users, 200)
# # for liking in likings:
# #     print(liking)


# log = likings + friendings + posts
# shuffle(log)
# with open("log2.txt", "w") as f:
#     f.writelines(log)
#
