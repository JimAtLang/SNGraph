from collections import deque
from typing import List, Set
from User import User

def get_connected_users_within_range(start_user: User, max_depth: int) -> List[User]:
    """
    Performs a BFS to find all users connected to `start_user`
    within `max_depth` edges (inclusive).
    """
    visited: Set[User] = set()
    queue = deque([(start_user, 0)])
    connected_users: List[User] = []

    while queue:
        current_user, depth = queue.popleft()

        if current_user in visited:
            continue

        visited.add(current_user)

        # Skip adding the starting user to the result
        if depth > 0:
            connected_users.append(current_user)

        # Stop searching deeper if we've reached the max depth
        if depth < max_depth:
            for neighbor in current_user.edges:
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))

    return connected_users