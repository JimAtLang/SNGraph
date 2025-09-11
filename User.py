from xmlrpc.client import DateTime
from typing import Dict, List, Self



class User:
    def __init__(self, name: str):
        self.name:str = name
        self.edges:Dict[Self, DateTime] = {}

    def add_edge(self, user:Self, time:DateTime):
        self.edges[user] = time
        user.add_edge(self, time)