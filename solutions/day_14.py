import time
import re
from collections import Counter
from typing import Any
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    lines = [[int(x) for x in l] for l in re.findall(pattern, data)]
    return lines


def final_pos(px, py, vx, vy, times, width, tall):
    fx = (px + (times * vx)) % width
    fy = (py + (times * vy)) % tall
    return (fx, fy)


def get_quadrant(x, y, width, tall):
    half_w = width // 2
    half_t = tall // 2
    # north east
    if 0 <= y < half_t and half_w < x < width:
        return "NE"
    # north west
    if 0 <= y < half_t and 0 <= x < half_w:
        return "NW"
    # south east
    if half_t < y < tall and half_w < x < width:
        return "SE"
    # south west
    if half_t < y < tall and 0 <= x < half_w:
        return "SW"


def print_matrix(m, width, tall):
    res = ""
    for y in range(tall):
        for x in range(width):
            # if x == width//2 or y == tall//2:
            #    res += 'X'
            #   continue
            if (x, y) in m:
                res += "█"  # str(m[(x, y)])
            else:
                res += "."
        res += "\n"
    print(res)
    return res


def solve_part1(parsed_data: Any, width=101, tall=103) -> Any:
    """Solve part 1 of the puzzle."""
    quadrant_count = Counter()
    times = 100
    mapa = Counter()
    for px, py, vx, vy in parsed_data:
        x, y = final_pos(px, py, vx, vy, times, width, tall)
        mapa[(x, y)] += 1
        quadrant_count[get_quadrant(x, y, width, tall)] += 1
        print(x, y, "for", px, py, vx, vy, get_quadrant(x, y, width, tall))

    print_matrix(mapa, width, tall)
    return (
        quadrant_count["NE"]
        * quadrant_count["NW"]
        * quadrant_count["SE"]
        * quadrant_count["SW"]
    )
    # 230211072 too low


def find_rectangle_area(points):
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)

    width = max_x - min_x
    height = max_y - min_y
    return width * height


def solve_part2(parsed_data: Any, width=101, tall=103) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    clear_screen()
    min_area = float("Inf")
    for t in range(112, 10000, 101):
        mapa = Counter()
        quadrant_count = Counter()
        for px, py, vx, vy in parsed_data:
            x, y = final_pos(px, py, vx, vy, t, width, tall)
            mapa[(x, y)] += 1
            quadrant_count[get_quadrant(x, y, width, tall)] += 1

        # clear_screen()
        print_matrix(mapa, width, tall)
        print(t)
    return 0


# Uncomment and modify test data as needed
test_input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_14.txt", "r") as f:
        input_data = f.read().strip()

    # Parse input
    parsed_data = parse_input(input_data)

    # Optional: Run tests
    if "test_input" in globals():
        print("🧪 Running tests...")
        test_parsed = parse_input(test_input)
        print(f"Test Part 1: {solve_part1(test_parsed, width=11, tall =7)}")
        # print(f"Test Part 2: {solve_part2(test_parsed)}")
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
