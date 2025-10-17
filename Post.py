from datetime import datetime

class Post:
    def __init__(self, author, post_format:str, subject:str, post_date:datetime):
        self.author = author
        self.format:str = post_format
        self.subject:str = subject
        self.post_date: datetime = post_date
        self.likes:int = 0
        self.reposts:int = 0
        self.popularity:int = 0

    def like(self, user)->None:
        self.likes += 1
        self.popularity += 1

    def repost(self, user)->None:
        self.reposts += 1
        self.popularity += 2
