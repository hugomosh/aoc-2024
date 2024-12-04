from collections import Counter
from typing import Any
import time


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.strip().split("\n")
    list1 = []
    list2 = []
    for line in lines:
        e1, e2 = map(int, line.split())
        list1.append(e1)
        list2.append(e2)
    return (list1, list2)


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    list1, list2 = parsed_data
    list1.sort()
    list2.sort()
    diff = sum(abs(e2 - e1) for e1, e2 in zip(list1, list2))
    print(diff)
    return diff


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    list1, list2 = parsed_data
    countl2 = Counter(list2)
    return sum(a * countl2[a] for a in list1)


# Uncomment and modify test data as needed
test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_1.txt", "r") as f:
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
