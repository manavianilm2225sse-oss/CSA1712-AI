import heapq

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Calculate Manhattan distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            value = state[i]
            goal_index = value - 1

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append((tuple(new_state), move))

    return neighbors


# A* Search
def solve_puzzle(start):
    priority_queue = []

    # (f(n), g(n), state, path)
    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start, [])
    )

    visited = set()

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if current == GOAL:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, move in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [move])
                )

    return None


# Display puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


# Main program
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

print("Initial State:")
display(start)

solution = solve_puzzle(start)

if solution is not None:
    print("Solution found!")
    print("Number of moves:", len(solution))
    print("Moves:", solution)

    # Display each state
    current = start

    for move in solution:
        for neighbor, m in get_neighbors(current):
            if m == move:
                current = neighbor
                print("\nMove:", move)
                display(current)
                break
else:
    print("No solution exists.")
