import time
from typing import Any
from collections import defaultdict


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    return [int(x) for x in data.strip()]


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    full = []
    for i, num in enumerate(parsed_data):
        file = i // 2 if i % 2 == 0 else -1
        for _ in range(num):
            full.append(file)
    while -1 in full:
        if full[-1] == -1:
            full.pop()
        else:
            index = full.index(-1)
            full[index] = full.pop()
    return sum(i * x for i, x in enumerate(full))


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    full = []
    sizes = []
    mapa = defaultdict(list)
    empty = []
    for i, num in enumerate(parsed_data):
        file = i // 2 if i % 2 == 0 else -1
        if file == -1:
            empty.append((len(full), num))
        else:
            sizes.append(num)
        for _ in range(num):
            full.append(file)
            mapa[file].append(len(full) - 1)
    while sizes:
        size = sizes.pop()
        file = len(sizes)
        for i, (index, e) in enumerate(empty):
            if index > mapa[file][0]:
                break
            if size <= e:
                for x in mapa[file]:
                    full[x] = -1
                for n in range(size):
                    full[index + n] = file
                empty[i] = (index + size, e - size)
                break

    # print("".join(map(str, full)))

    return sum(i * x if x != -1 else 0 for i, x in enumerate(full))


# Uncomment and modify test data as needed
test_input = """2333133121414131402
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_9.txt", "r") as f:
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
