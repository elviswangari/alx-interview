#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    function to check whether all the boxes have been opened or can they be
    opened with the provided key
    """

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    seque_line = [0]

    while seque_line:
        box = seque_line.pop(0)
        for item in boxes[box]:
            if item >= 0 and item < n and not visited[item]:
                visited[item] = True
                seque_line.append(item)

    return all(visited)
