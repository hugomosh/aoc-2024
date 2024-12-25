import time
from typing import Any
from itertools import product


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    schemas = data.strip().split("\n\n")
    locks = []
    keys = []
    for x in schemas:
        # code, is_lock
        for i, row in enumerate(x.splitlines()):
            if i == 0:
                code = [-1] * len(row)
                is_lock = row[0] == "."
            for j, col in enumerate(row.strip()):
                if col == "#":
                    code[j] += 1
        if is_lock:
            locks.append(code)
        else:
            keys.append(code)

    return (locks, keys)


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    (locks, keys) = parsed_data
    res = 0
    for l, k in product(locks, keys):
        sumed = [x + y for x, y in zip(l, k)]
        if max(sumed) <= 5:
            res += 1
    return res


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    # TODO: Implement solution
    return 0


# Uncomment and modify test data as needed
test_input = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_25.txt", "r") as f:
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
