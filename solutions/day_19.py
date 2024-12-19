import time
import re
from typing import Any
from functools import lru_cache


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    blocks, lines = data.strip().split("\n\n")
    blocks = [b for b in blocks.split(", ")]
    blocks.sort()
    lines = lines.splitlines()
    print(blocks, lines)
    return (blocks, lines)


def solve_part1_regex(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    (blocks, lines) = parsed_data

    def can_be_formed(line):
        dp = [False] * (len(line) + 1)
        dp[0] = True  # Empty string can be formed

        for i in range(len(line)):
            if not dp[i]:
                continue

            for block in blocks:
                if (
                    i + len(block) <= len(line)  # Check if block fits
                    and line[i : i + len(block)] == block
                ):  # Check exact match
                    dp[i + len(block)] = True

        return dp[len(line)]

    matches = [line for line in lines if can_be_formed(line)]
    # print(matches)
    return len(matches)


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    (blocks, lines) = parsed_data

    @lru_cache
    def count_options(line):
        if line == "":
            return 1
        count = 0
        for block in blocks:
            if (
                len(block) <= len(line)  # Check if block fits
                and line[: len(block)] == block
            ):
                count += count_options(line[len(block) :])

        return count

    matches = [count_options(line) for line in lines]
    # print(matches)
    return sum(matches)

# With the help of Claude on this one
def solve_part2_print_all(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    (blocks, lines) = parsed_data

    @lru_cache
    def get_combinations(line):
        if line == "":
            return [[]]  # Return a list containing an empty combination

        combinations = []
        for block in blocks:
            if (len(block) <= len(line) and line[:len(block)] == block):
                # Get all combinations for the rest of the string
                rest_combinations = get_combinations(line[len(block):])
                # Add current block to each combination
                for combo in rest_combinations:
                    combinations.append([block] + combo)

        return combinations

    matches = [get_combinations(line) for line in lines]
    # Print them to see the structure
    for line, combos in zip(lines, matches):
        print(f"\n{line}:")
        for combo in combos:
            print(f"  {combo}")

    return sum(len(m) for m in matches)

# Uncomment and modify test data as needed
test_input = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_19.txt", "r") as f:
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
