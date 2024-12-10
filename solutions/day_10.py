import time
from typing import Any
from collections import defaultdict


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.split("\n")

    return [[int(x) for x in l] for l in lines]


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    simbols = defaultdict(list)
    mapa = {}
    for row, line in enumerate(parsed_data):
        for col, e in enumerate(line):
            mapa[(row, col)] = e
            simbols[e].append((row, col))
    directions = [
        # (-1, -1),  # Top-left
        (-1, 0),  # Top
        # (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),  # Right
        # (1, -1),  # Bottom-left
        (1, 0),  # Bottom
        # (1, 1),  # Bottom-right
    ]
    # BFS or DFS
    res = 0
    paths = []
    trails = set()
    queue = [[x] for x in simbols[0]]

    while queue:
        current = queue.pop()
        next_height = len(current)
        for r, c in directions:
            n = (current[-1][0] + r, current[-1][1] + c)
            if mapa.get(n) == next_height:
                # print(n, next_height, current)
                copy = current[:]
                copy.append(n)
                if next_height == 9:
                    res += 1
                    paths.append(copy)
                    trails.add(f"{copy[0]},{copy[-1]}")
                else:
                    queue.append(copy)
    # print(trails)
    return len(trails)


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    simbols = defaultdict(list)
    mapa = {}
    for row, line in enumerate(parsed_data):
        for col, e in enumerate(line):
            mapa[(row, col)] = e
            simbols[e].append((row, col))
    directions = [
        # (-1, -1),  # Top-left
        (-1, 0),  # Top
        # (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),  # Right
        # (1, -1),  # Bottom-left
        (1, 0),  # Bottom
        # (1, 1),  # Bottom-right
    ]
    # BFS or DFS
    res = 0
    paths = []
    trails = set()
    queue = [[x] for x in simbols[0]]

    while queue:
        current = queue.pop()
        next_height = len(current)
        for r, c in directions:
            n = (current[-1][0] + r, current[-1][1] + c)
            if mapa.get(n) == next_height:
                # print(n, next_height, current)
                copy = current[:]
                copy.append(n)
                if next_height == 9:
                    res += 1
                    paths.append(copy)
                    trails.add(f"{copy[0]},{copy[-1]}")
                else:
                    queue.append(copy)
    # print(trails)
    return res


# Uncomment and modify test data as needed
test_input23 = """0123
1234
8765
9876
"""
test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_10.txt", "r") as f:
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
