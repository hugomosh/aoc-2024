import time
from typing import Any
from collections import deque


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.strip().splitlines()
    mapa = {}
    for y, l in enumerate(lines):
        for x, e in enumerate(l):
            mapa[x + y * 1j] = e
            if e == "S":
                start = x + y * 1j
            elif e == "E":
                goal = x + y * 1j
    return (mapa, start, goal)


def possible_directions(node, mapa):
    directions = [1, 1j, -1j]
    res = []
    for d in directions:
        new_pos = node[0] + d * node[1]
        if new_pos in mapa and mapa[new_pos] in [".", "E"]:
            res.append((new_pos, d * node[1]))
    return res


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    (mapa, start, goal) = parsed_data

    visited = {}  # to keep cost
    visited[(start, 1)] = 0
    queue = [(start, 1)]  # facing east
    while queue:
        c = queue.pop(0)
        if mapa[c[0]] == "E":
            print(c, visited[c])
        for n, d in possible_directions(c, mapa):
            cost = 1 if d == c[1] else 1001
            if (n, d) in visited:
                if visited[(n, d)] > visited[c] + cost:
                    visited[(n, d)] = visited[c] + cost
                    if not (n, d) in queue:
                        queue.append((n, d))
                continue
            else:
                visited[(n, d)] = visited[c] + cost
            queue.append((n, d))

    best = float("Inf")
    best_x = None
    for x in visited.keys():
        if x[0] == goal:
            if best > visited[x]:
                best = visited[x]
                best_x = x

    return best


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    (mapa, start, goal) = parsed_data

    visited = {}  # to keep cost
    visited[(start, 1)] = 0
    queue = deque([(start, 1)])  # facing east
    while queue:
        c = queue.popleft()
        for n, d in possible_directions(c, mapa):
            cost = 1 if d == c[1] else 1001
            if (n, d) in visited:
                if visited[(n, d)] > visited[c] + cost:
                    visited[(n, d)] = visited[c] + cost
                    if not (n, d) in queue:
                        queue.append((n, d))
                continue
            else:
                visited[(n, d)] = visited[c] + cost
            queue.append((n, d))

    best = float("Inf")
    best_x = None
    for x in visited.keys():
        if x[0] == goal:
            if best > visited[x]:
                best = visited[x]
                best_x = x

    # Backwards search using possible previous positions
    next_level = deque([best_x])
    spots = {best_x[0]}
    seen_states = {best_x}  # Prevent revisiting same state

    while next_level:
        current_pos, current_dir = next_level.popleft()
        current_cost = visited[(current_pos, current_dir)]

        # Calculate possible previous positions
        # For complex numbers, possible moves are ±1 and ±1j
        possible_prev = [current_pos + d for d in [1, -1, 1j, -1j]]

        for prev_pos in possible_prev:
            # For each possible previous position, check both same direction and turn
            for prev_dir in [current_dir, 1j * current_dir, -1j * current_dir]:
                prev_state = (prev_pos, prev_dir)
                if (
                    prev_state in visited
                    and prev_state not in seen_states
                    and visited[prev_state] + (1 if prev_dir == current_dir else 1001)
                    == current_cost
                ):
                    next_level.append(prev_state)
                    seen_states.add(prev_state)
                    spots.add(prev_pos)

    return len(spots)


# Uncomment and modify test data as needed
test_input = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_16.txt", "r") as f:
        input_data = f.read().strip()

    # Parse input
    parsed_data = parse_input(input_data)

    # Optional: Run tests
    if "test_input" in globals():
        print("🧪 Running tests...")
        test_parsed = parse_input(test_input)
        print(f"Test Part 1: {solve_part1(test_parsed)}")
        print(f"Test Part 2: {solve_part2(test_parsed)}")
        print()

    # Solve part 1
    start_time = time.time()
    answer1 = solve_part1(parsed_data)
    time1 = time.time() - start_time
    print(f"✨ Part 1 answer: {answer1} (took {time1:.2f}s)\n")
    # too high 126456

    # Solve part 2
    start_time = time.time()
    answer2 = solve_part2(parsed_data)
    time2 = time.time() - start_time
    print(f"✨ Part 2 answer: {answer2} (took {time2:.2f}s)")
