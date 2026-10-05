from collections import deque

# State = (Missionaries on left, Cannibals on left, Boat side)
# Boat side: 0 = Left, 1 = Right

def is_valid(m, c):
    # Total missionaries and cannibals = 3 each
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Missionaries should not be outnumbered by cannibals
    if m > 0 and m < c:
        return False

    # Check the right side
    mr = 3 - m
    cr = 3 - c

    if mr > 0 and mr < cr:
        return False

    return True


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    # Possible boat movements
    moves = [
        (1, 0),  # 1 Missionary
        (2, 0),  # 2 Missionaries
        (0, 1),  # 1 Cannibal
        (0, 2),  # 2 Cannibals
        (1, 1)   # 1 Missionary and 1 Cannibal
    ]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        for dm, dc in moves:
            if boat == 0:       # Boat moves from Left to Right
                new_state = (m - dm, c - dc, 1)
            else:               # Boat moves from Right to Left
                new_state = (m + dm, c + dc, 0)

            nm, nc, nb = new_state

            if is_valid(nm, nc) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No solution found.")


solve()
