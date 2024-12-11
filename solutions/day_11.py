import time
from typing import Any
from collections import defaultdict
from functools import lru_cache


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = [int(x) for l in data.strip().split("\n") for x in l.split()]
    # TODO: Modify parsing logic
    print(lines)
    return lines


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    old = parsed_data
    for n in range(25):
        nl = []
        for x in old:
            if x == 0:
                nl.append(1)
            elif len(str(x)) % 2 == 0:
                s = str(x)
                mid = len(s) // 2
                nl.append(int(str(x)[:mid]))
                nl.append(int(str(x)[mid:]))
            else:
                nl.append(2024 * x)
        old = nl
        # print(n)
    return len(nl)


"""dumb attempt to memoize
class Level:
    memory = {}  # Change to tuple (number, level) -> result

    def __init__(self, number, level):
        self.number = number
        self.level = level
        self.stones_per_level = [1]
        self.current = [self]

    def __new__(cls, number, level):
        # Use both number and level as cache key
        cache_key = (number, level)

        if cache_key in Level.memory:
            return Level.memory[cache_key]

        # Create new instance
        instance = super().__new__(cls)
        instance.__init__(number, level)

        # Cache the result
        Level.memory[cache_key] = instance

        # Optional: Add basic LRU functionality
        if len(Level.memory) > 10000:  # Arbitrary limit
            # Remove oldest entry
            oldest_key = next(iter(Level.memory))
            del Level.memory[oldest_key]

        while len(instance.stones_per_level) < level:
            instance.next_level()

        return instance

    def next_level(self):
        nl = []
        next_l = self.level - 1
        for l in self.current:
            x = l.number
            if x == 0:
                nl.append(Level(1, next_l))
            elif len(str(x)) % 2 == 0:
                s = str(x)
                mid = len(s) // 2
                nl.append(Level(int(str(x)[:mid]), next_l))
                nl.append(Level(int(str(x)[mid:]), next_l))
            else:
                nl.append(Level(2024 * x, next_l))

        self.current = nl
        self.stones_per_level.append(len(nl))


def solve_part2(parsed_data: Any) -> Any:
    print("🎯 Solving part 2...")

    res = 0
    for x in parsed_data:
        l = Level(x, 25)
        print(len(l.stones_per_level))
        res += l.stones_per_level[-1]

    return res

"""


@lru_cache(maxsize=None)
def process_number(num: int, level: int) -> int:
    """
    Process a single number and return how many numbers it will generate at the target level.
    Uses memoization to cache results for repeated calculations.
    """
    # Base case - reached target level
    if level == 0:
        return 1

    # Process number according to rules
    if num == 0:
        return process_number(1, level - 1)
    elif len(str(num)) % 2 == 0:
        s = str(num)
        mid = len(s) // 2
        left = int(s[:mid])
        right = int(s[mid:])
        return process_number(left, level - 1) + process_number(right, level - 1)
    else:
        return process_number(2024 * num, level - 1)


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 using memoization."""
    print("🎯 Solving part 2...")

    total = 0
    for num in parsed_data:
        count = process_number(num, 75)
        total += count

    print(process_number.cache_info())
    return total


# # Uncomment and modify test data as needed
test_input = """
125 17
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_11.txt", "r") as f:
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
