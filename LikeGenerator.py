from math import floor

from User import User
from typing import List
from random import choice
from BFSTraverser import get_connected_users_within_range

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
        likes.append(f"{liker.name} liked {post.author.name}'s {post.format} meme about {post.subject}")
    return likes