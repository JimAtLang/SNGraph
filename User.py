from xmlrpc.client import DateTime
from typing import Dict, List, Self

class User:
    def __init__(self, name: str):
        self.name:str = name
        self.edges:List[Self] = []

    def add_edge(self, user:Self):
        self.edges.append(user)

    def delete_edge(self, user:Self):
        if user in self.edges:
            self.edges.remove(user)
        user.remove_edge(self)