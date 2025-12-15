from typing import TextIO
from datetime import datetime, timedelta
from random import choice
from DateGenerator import random_date
from User import User

start_date:datetime = datetime(2020, 1, 1)


def get_post(users, date):
    f:TextIO

    meme_formats = []
    meme_subjects = []
    posts = []
    with open("meme_formats.txt","r") as f:
        meme_formats = f.readlines()

    with open("meme_subjects.txt","r") as f:
        meme_subjects = f.readlines()


    user:User = choice(users)
    post_format = choice(meme_formats).strip()
    subject = choice(meme_subjects).strip()
    user.post(post_format, subject, start_date)
    return f"{user.name} posted a {post_format} meme about {subject} on {date:%B %d, %Y}\n"


def get_posts(users, count):
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
        post_time:datetime = random_date(start_date, start_date + timedelta(days=5))
        post_format = choice(meme_formats).strip()
        subject = choice(meme_subjects).strip()
        user.post(post_format, subject, post_time)
        posts.append(f"{user.name} posted a {post_format} meme about {subject} on {post_time:%B %d, %Y}\n")
    return posts
