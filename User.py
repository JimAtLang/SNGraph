from datetime import datetime
from typing import Dict, List, Self
from Post import Post

class User:
    def __init__(self, name: str):
        self.name:str = name
        self.edges:List[Self] = []
        self.timeline:Dict[Post, datetime] = {}

    def add_edge(self, user:Self)->None:
        self.edges.append(user)

    def delete_edge(self, user:Self)->None:
        if user in self.edges:
            self.edges.remove(user)
        user.remove_edge(self)

    def like_post(self, post:Post)->None:
        post.like(self)

    def repost(self, post:Post, time:datetime)->None:
        post.repost(self)
        self.timeline[post] = time

    def post(self, post_format:str, subject:str, post_time:datetime)->Post:
        post=Post(self, post_format, subject, post_time)
        self.timeline[post]=post_time
        return post
