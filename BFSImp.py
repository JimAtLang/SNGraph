from random import choice
from typing import List, Dict
from random import choice
from User import User


def get_user_in_range(poster:User, rng:int, users:List[User]) -> User:
    visited: Dict[User, int] = {}
    dist = 0
    for friend in users:
        visited[friend] = 0
    visited[poster] = 0
    queue: List[User] = [poster]
    audience:List[User] = []
    while queue:
        friend: User = queue.pop(0)
        audience.append(friend)
        if visited[friend] < rng:
            for edge in friend.edges:
                if not (visited[edge] or edge is poster):
                    queue.append(edge)
                    visited[edge] = visited[friend] + 1
    return choice(audience)