import time
import cmath
from typing import Dict, Any


def parse_input(data: str) -> Dict[complex, str]:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    mapa = {}
    for x, row in enumerate(data.strip().splitlines()):
        for y, e in enumerate(row):
            mapa[x + y * 1j] = e
    return mapa


def get_neighbors(current, mapa):
    directions = [-1, 1j, 1, -1j]
    return [current + d for d in directions if current + d in mapa]


def get_corners(current, mapa):
    res = 0
    v = mapa[current]
    DOWN = 1 + 0j
    UP = -1 + 0j
    RIGHT = 0 + 1j
    LEFT = 0 - 1j

    # Use a default that won't match v
    def get_val(pos):
        return mapa.get(pos, None)

    # Top Left corners
    if (
        get_val(current + UP) == v
        and get_val(current + LEFT) == v
        and get_val(current + UP + LEFT) != v
    ):
        # left top inverse corner
        res += 1
    if (
        get_val(current + UP) != v
        and get_val(current + LEFT) != v
    ):
        # left top inside corner
        res += 1

    # Top Right corners
    if (
        get_val(current + UP) == v
        and get_val(current + RIGHT) == v
        and get_val(current + UP + RIGHT) != v
    ):
        # right top inverse corner
        res += 1
    if (
        get_val(current + UP) != v
        and get_val(current + RIGHT) != v
    ):
        # right top inside corner
        res += 1

    # Bottom Left corners
    if (
        get_val(current + DOWN) == v
        and get_val(current + LEFT) == v
        and get_val(current + DOWN + LEFT) != v
    ):
        # left bottom inverse corner
        res += 1
    if (
        get_val(current + DOWN) != v
        and get_val(current + LEFT) != v
    ):
        # left bottom inside corner
        res += 1

    # Bottom Right corners
    if (
        get_val(current + DOWN) == v
        and get_val(current + RIGHT) == v
        and get_val(current + DOWN + RIGHT) != v
    ):
        # right bottom inverse corner
        res += 1
    if (
        get_val(current + DOWN) != v
        and get_val(current + RIGHT) != v
    ):
        # right bottom inside corner
        res += 1

    return res


def solve_part1(mapa: Dict[complex, str]) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    unvisited = set(mapa.keys())
    res = 0
    zones = []
    while unvisited:
        new_zone = unvisited.pop()
        zone_val = mapa[new_zone]
        area = 0
        perimeter = 0
        queue = set([new_zone])
        while queue:
            current = queue.pop()
            unvisited.discard(current)
            neighbors = get_neighbors(current, mapa)
            area += 1
            perimeter += 4
            for x in neighbors:
                if mapa[x] == zone_val:
                    perimeter -= 1
                    if x in unvisited:
                        queue.add(x)
        # print(zone_val, area, perimeter)
        res += area * perimeter

    return res


def solve_part2(mapa: Dict[complex, str]) -> Any:
    """Solve part 2 of the puzzle."""
    unvisited = set(mapa.keys())
    res = 0
    zones = []
    while unvisited:
        new_zone = unvisited.pop()
        zone_val = mapa[new_zone]
        area = 0
        perimeter = 0
        queue = set([new_zone])
        corners = 0
        while queue:
            current = queue.pop()
            unvisited.discard(current)
            neighbors = get_neighbors(current, mapa)
            area += 1
            new_perimeter = 4
            for x in neighbors:
                if mapa[x] == zone_val:
                    new_perimeter -= 1
                    if x in unvisited:
                        queue.add(x)
            perimeter += new_perimeter
            corners += get_corners(current, mapa)

        # Navigate perimeter zxz
        print(zone_val, area, perimeter, corners)
        res += area * corners

    return res


# Uncomment and modify test data as needed
test_input2 = """AAAA
BBCD
BBCC
EEEC
"""
test_input = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""
test_input1 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_12.txt", "r") as f:
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
    # 891638 too low
