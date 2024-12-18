import time
from typing import Any

def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.split("\n")
    m = [list(line) for line in lines]
    return m


def within_range(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def try_all_directions(row, col, data):
    directions = [
        (-1, -1),  # Top-left
        (-1, 0),  # Top
        (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Bottom-left
        (1, 0),  # Bottom
        (1, 1),  # Bottom-right
    ]
    word = ["M", "A", "S"]
    res = []
    for dr, dc in directions:
        if all(
            within_range(row + i * dr, col + i * dc, data)
            and data[row + i * dr][col + i * dc] == letter
            for i, letter in enumerate(word, 1)
        ):
            res.append((dr, dc))
    return res


def try_mas(row, col, data):
    directions = [
        (-1, -1),  # Top-left
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
        (1, 1),  # Bottom-right
    ]
    word = ["M", "A", "S"]
    res = list()
    valid = True
    for dr, dc in directions:
        if not within_range(row + dr, col + dc, data):
            return 0

    if (
        data[row - 1][col - 1] == "M"
        and data[row + 1][col + 1] == "S"
        or data[row - 1][col - 1] == "S"
        and data[row + 1][col + 1] == "M"
    ) and (
        data[row - 1][col + 1] == "M"
        and data[row + 1][col - 1] == "S"
        or data[row - 1][col + 1] == "S"
        and data[row + 1][col - 1] == "M"
    ):
        return 1

    return 0


def solve_part1(data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    count = 0
    for i, row in enumerate(data):
        for j, e in enumerate(row):
            if e == "X":
                count += len(try_all_directions(i, j, data))
    return count


def solve_part2(data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    count = 0
    for i, row in enumerate(data):
        for j, e in enumerate(row):
            if e == "A":
                count += try_mas(i, j, data)
    return count


# Uncomment and modify test data as needed
test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_4.txt", "r") as f:
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
