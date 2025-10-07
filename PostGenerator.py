from typing import TextIO
from datetime import datetime
from random import choice
from DateGenerator import random_date
from User import User

start_date:datetime = datetime(2020, 1, 1)


def getPosts(users, count):
    f:TextIO

    meme_formats = []
    meme_subjects = []
    posts = []
    with open("meme_formats.txt","r") as f:
        meme_formats = f.readlines()

    with open("meme_subjects.txt","r") as f:
        meme_subjects = f.readlines()

    for i in range(count):
        user:User = choice(users)
        post_time:datetime = random_date(start_date, datetime.now())
        format = choice(meme_formats)
        subject = choice(meme_subjects)
        posts.append(f"{user.name} posted a {format} meme about {subject} on {post_time::%B %d, %Y}")
    return posts
