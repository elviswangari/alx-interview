#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    function to check whether all the boxes have been opened or can they be
    opened with the provided key
    """

    n = len(boxes)
    visited = set()
    visited.add(0)
    queue = [0]
    front = 0  # Index to keep track of the front of the queue

    while front < len(queue):
        box = queue[front]
        for item in boxes[box]:
            if item < n and item not in visited:
                visited.add(item)
                queue.append(item)
        front += 1

    return len(visited) == n
