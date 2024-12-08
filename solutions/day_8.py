import time
from typing import Any
from collections import defaultdict
import itertools


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.split("\n")
    return lines


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    mapa = {}
    obs = defaultdict(list)
    for row, l in enumerate(parsed_data):
        for col, char in enumerate(l):
            mapa[(row, col)] = char
            obs[char].append((row, col))

    antinodes = set()
    for key, vals in obs.items():
        if key == ".":
            continue
        # print(key,vals)
        for combo in itertools.combinations(vals, 2):
            (a1, a2), (b1, b2) = combo
            x = a1 - b1
            y = a2 - b2
            prev1 = (a1 + x, a2 + y)
            prev2 = (b1 - x, b2 - y)
            # print(combo,  prev1, prev2)
            if prev1 in mapa:
                antinodes.add(prev1)
            if prev2 in mapa:
                antinodes.add(prev2)

    return len(antinodes)


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    mapa = {}
    obs = defaultdict(list)
    for row, l in enumerate(parsed_data):
        for col, char in enumerate(l):
            mapa[(row, col)] = char
            obs[char].append((row, col))

    antinodes = set()
    for key, vals in obs.items():
        if key == ".":
            continue
        # print(key,vals)
        for combo in itertools.combinations(vals, 2):
            (a1, a2), (b1, b2) = combo
            a, b = combo
            antinodes.add(a)
            antinodes.add(b)
            x = a1 - b1
            y = a2 - b2
            prev1 = (a1 + x, a2 + y)
            prev2 = (b1 - x, b2 - y)
            # print(combo,  prev1, prev2)
            while prev1 in mapa:
                antinodes.add(prev1)
                prev1 = (prev1[0] + x, prev1[1] + y)
            while prev2 in mapa:
                antinodes.add(prev2)
                prev2 = (prev2[0] - x, prev2[1] - y)
    return len(antinodes)


# Uncomment and modify test data as needed
test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
t2 = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........
"""
if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_8.txt", "r") as f:
        input_data = f.read().strip()

    # Parse input
    parsed_data = parse_input(input_data)

    # Optional: Run tests
    if "test_input" in globals():
        print("🧪 Running tests...")
        test_parsed = parse_input(test_input)
        print(f"Test Part 1: {solve_part1(test_parsed)}")
        print(f"Test Part 2: {solve_part2(test_parsed)}")
        print(f"Test Part 2: {solve_part2(parse_input(t2))}")

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
