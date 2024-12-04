from datetime import datetime
from typing import Any
import time
import re


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    lines = data.split("\n")
    """ for l in lines:
      matches = re.findall(pattern, l)
      print(matches) """
    return matches


def parse_input2(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input 2...")
    pattern = r"mul\((\d+),(\d+)\)"
    sections = re.split(r"(do\(\)|don't\(\))", data)
    enabled = True
    m = []
    for s in sections:
        if s == "do()" or s == "don't()":
            enabled = s == "do()"
            continue
        if enabled:
            m = m + re.findall(pattern, s)

    return m


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    total = sum(int(x) * int(y) for x, y in parsed_data)
    return total


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    total = sum(int(x) * int(y) for x, y in parsed_data)
    return total


# Uncomment and modify test data as needed
test_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
test_input2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_3.txt", "r") as f:
        input_data = f.read().strip()

    # Parse input
    parsed_data = parse_input(input_data)

    # Optional: Run tests
    if "test_input" in globals():
        print("🧪 Running tests...")
        test_parsed = parse_input(test_input)
        test_parsed2 = parse_input2(test_input2)
        print(f"Test Part 1: {solve_part1(test_parsed)}")
        print(f"Test Part 2: {solve_part2(test_parsed2)}")
        print()

    # Solve part 1
    start_time = time.time()
    answer1 = solve_part1(parsed_data)
    time1 = time.time() - start_time
    print(f"✨ Part 1 answer: {answer1} (took {time1:.2f}s)\n")

    # Solve part 2
    start_time = time.time()
    answer2 = solve_part2(parse_input2(input_data))
    time2 = time.time() - start_time
    print(f"✨ Part 2 answer: {answer2} (took {time2:.2f}s)")
