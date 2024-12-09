import time
from typing import Any
from collections import defaultdict


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.split("\n")
    # TODO: Modify parsing logic
    return lines[0]


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    index = 0
    files = defaultdict(list)
    ff = []
    full = []
    for i, char in enumerate(parsed_data):
        num = int(char)
        if i % 2 == 0:
            # file
            file = i // 2
            for x in range(num):
                print(file)
                files[file].append(index)
                full.append(file)
                index += 1
            ff.append(files[file])
        else:
            # free
            for x in range(num):
                files["."].append(index)
                full.append(".")
                index += 1
    print(files, ff, full)
    queue = ff.pop(-1)[:]
    index = len(ff)
    for free_space in files["."]:
        if not queue:
            queue = ff.pop(-1)[:]
            index = len(ff)
        change = queue.pop(-1)
        index_in_file = len(queue)
        if files[index][index_in_file] <= free_space:
            break
        files[index][index_in_file] = free_space
    if queue:
        files[index] = queue
    res = 0
    for key, vals in files.items():
        if key == ".":
            continue
        res += sum([v * key for v in vals])
    return res


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    # TODO: Implement solution
    return 0


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
    #answer1 = solve_part1(parsed_data)
    time1 = time.time() - start_time
    print(f"✨ Part 1 answer: {answer1} (took {time1:.2f}s)\n")

    # Solve part 2
    start_time = time.time()
    answer2 = solve_part2(parsed_data)
    time2 = time.time() - start_time
    print(f"✨ Part 2 answer: {answer2} (took {time2:.2f}s)")
