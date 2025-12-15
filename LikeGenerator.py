from math import floor
from User import User
from typing import List
from random import choice
from BFSTraverser import get_connected_users_within_range

def make_like(users: List[User], date) -> str:
    user = User("")
    while len(user.edges)==0 or len(user.timeline)==0:
        user = choice(users)
    post = choice(list(user.timeline.keys()))
    dist = int(floor(post.likes/5 + post.reposts/3)+1)
    friends = get_connected_users_within_range(user, dist)
    liker = choice(friends)
    liker.like_post(post)
    return  f"{liker.name} liked {post.author.name}'s {post.format} meme about {post.subject} on {date:%B %d, %Y}\n"

def make_repost(users: List[User], date) -> str:
    user = User("")
    while len(user.edges)==0 or len(user.timeline)==0:
        user = choice(users)
    post = choice(list(user.timeline.keys()))
    dist = int(floor(post.likes/5 + post.reposts/3)+1)
    friends = get_connected_users_within_range(user, dist)
    liker = choice(friends)
    liker.repost(post,date)
    return  f"{liker.name} reposted {post.author.name}'s {post.format} meme about {post.subject} on {date:%B %d, %Y}\n"



def make_likes(users: List[User], count:int) -> List[str]:
    likes:List[str] = []
    for i in range(count):
        user = User("")
        while len(user.edges)==0:
            user = choice(users)
        post = choice(list(user.timeline.keys()))
        dist = int(floor(post.likes/5 + post.reposts/3)+1)
        friends = get_connected_users_within_range(user, dist)
        liker = choice(friends)
        liker.like_post(post)
        likes.append(f"{liker.name} liked {post.author.name}'s {post.format} meme about {post.subject}\n")
    return likes