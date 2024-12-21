import time
from typing import Any
from collections import defaultdict, Counter


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    mapa = {}

    blocks = defaultdict(list)
    for y, row in enumerate(data.strip().splitlines()):
        for x, e in enumerate(row):
            coords = x + y * 1j
            mapa[coords] = e
            blocks[e].append(coords)
    return (mapa, blocks)


def neighboars(current, mapa):
    directions = [1, -1, 1j, -1j]
    for d in directions:
        if mapa.get(current + d):
            yield current + d


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    (mapa, blocks) = parsed_data
    start = blocks["S"][0]
    end = blocks["E"][0]
    main = [start]

    while main[-1] != end:
        last = main[-1]

        for n in neighboars(last, mapa):
            if mapa[n] in ["E", "."] and not n in main:
                main.append(n)
                break

    len_main = len(main)

    # print(len_main)
    savings = []
    for i, coord in enumerate(main):
        for n1 in neighboars(coord, mapa):
            if mapa.get(n1) == "#":
                for n2 in neighboars(n1, mapa):
                    if n2 != coord and n2 in main:
                        i2 = main.index(n2)
                        if i2 - i - 2 > 0:
                            # print(coord, n2, i2, i, i2 - i - 2)
                            savings.append((i2 - i - 2))

    # print(savings, Counter(savings), len(savings))
    # return len(list(filter(lambda x: x >= 100, savings)))
    return sum(1 for amount in savings if amount >= 100)


# 1393
def distance(a, b):
    # Manhatthn
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    (mapa, blocks) = parsed_data
    start = blocks["S"][0]
    end = blocks["E"][0]
    main = [start]

    while main[-1] != end:
        last = main[-1]

        for n in neighboars(last, mapa):
            if mapa[n] in ["E", "."] and not n in main:
                main.append(n)
                break

    len_main = len(main)

    # print(len_main)
    savings = []
    for a, coordA in enumerate(main):
        for b, coordB in enumerate(main):
            if b <= a:
                continue
            d = distance(coordA, coordB)
            if d <= 20 and b - a - d > 0:
                #print(coordA, coordB, a, b, d, b - a + d)
                savings.append((b - a - d))

    #print(savings, Counter(savings), len(savings))
    #return len(list(filter(lambda x: x >= 100, savings)))
    return sum(1 for amount in savings if amount >= 100)


# Uncomment and modify test data as needed
test_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_20.txt", "r") as f:
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
    # answer1 = solve_part1(parsed_data)
    time1 = time.time() - start_time
    # print(f"✨ Part 1 answer: {answer1} (took {time1:.2f}s)\n")

    # Solve part 2
    start_time = time.time()
    answer2 = solve_part2(parsed_data)
    time2 = time.time() - start_time
    print(f"✨ Part 2 answer: {answer2} (took {time2:.2f}s)")
