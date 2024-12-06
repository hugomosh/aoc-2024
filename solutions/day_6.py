import time
import copy
from typing import Any

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def help():
    print(1836)


def add_tuples(tuple1, tuple2):
    return tuple(x + y for x, y in zip(tuple1, tuple2))


def inside(p, m):

    return 0 <= p[0] < len(m) and 0 <= p[1] < len(m[0])


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = [list(x) for x in data.strip().split("\n")]
    # print(lines)
    return lines


def solve_part1(matrix: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    origin = None

    for row_idx, row in enumerate(matrix):
        for col_idx, element in enumerate(row):
            if element == "^":
                origin = (row_idx, col_idx)
                break
        else:
            continue
    current_dir = 0
    positions = set()
    while True:
        positions.add(origin)
        next_pos = add_tuples(origin, directions[current_dir])
        if not inside(next_pos, matrix):
            break
        # print(origin, next_pos, matrix[next_pos[0]][next_pos[1]])
        while matrix[next_pos[0]][next_pos[1]] == "#":
            # Turn right
            current_dir = (current_dir + 1) % len(directions)
            next_pos = add_tuples(origin, directions[current_dir])
        origin = next_pos

    return len(positions)


def solve_loop(m: Any, origin, current_dir) -> Any:
    positions = set()
    while True:
        positions.add((origin, current_dir))
        next_pos = add_tuples(origin, directions[current_dir])
        if not inside(next_pos, m):
            return 0
        # print(origin, next_pos, m[next_pos[0]][next_pos[1]])
        while m[next_pos[0]][next_pos[1]] == "#":
            # Turn right
            current_dir = (current_dir + 1) % len(directions)
            next_pos = add_tuples(origin, directions[current_dir])
        origin = next_pos
        if (origin, current_dir) in positions:
            return 1
    return 0


def solve_part2(matrix: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    origin = None

    for row_idx, row in enumerate(matrix):
        for col_idx, element in enumerate(row):
            if element == "^":
                origin = (row_idx, col_idx)
                break
        else:
            continue
    original = origin
    current_dir = 0
    positions = set()
    while True:
        positions.add(origin)
        next_pos = add_tuples(origin, directions[current_dir])
        if not inside(next_pos, matrix):
            break
        # print(origin, next_pos, matrix[next_pos[0]][next_pos[1]])
        while matrix[next_pos[0]][next_pos[1]] == "#":
            # Turn right
            current_dir = (current_dir + 1) % len(directions)
            next_pos = add_tuples(origin, directions[current_dir])
        origin = next_pos
    count = 0
    for x in positions:
        if matrix[x[0]][x[1]] == ".":
            m = copy.deepcopy(matrix)
            m[x[0]][x[1]] = "#"
            # print('\n'.join(''.join(map(str, row)) for row in m))
            count += solve_loop(m, original, 0)
    return count


# Uncomment and modify test data as needed
test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_6.txt", "r") as f:
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

    # Solve part 2
    start_time = time.time()
    answer2 = solve_part2(parsed_data)
    time2 = time.time() - start_time
    print(f"✨ Part 2 answer: {answer2} (took {time2:.2f}s)")


help()
