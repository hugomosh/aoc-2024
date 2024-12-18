import time
from typing import Any
from collections import deque


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.strip().split("\n")
    coords = [int(x[0]) + int(x[1]) * 1j for x in [l.split(",") for l in lines]]
    return coords


def print_matrix(m, width, tall):
    res = ""
    for y in range(tall):
        for x in range(width):
            # if x == width//2 or y == tall//2:
            #    res += 'X'
            #   continue
            if m[(x + y * 1j)] == 0:
                res += "."  # str(m[(x, y)])
            else:
                res += "#"
        res += "\n"
    return res


def neighbors(c, mapa):
    directions = [1, -1, 1j, -1j]
    for d in directions:
        n = c + d
        if n in mapa and mapa[n] != 1:
            yield n


def solve_part1(parsed_data: Any, size=71, k=1024) -> Any:
    """Solve part 1 of the puzzle."""
    # print("🎯 Solving part 1...")
    start = 0
    goal = size - 1 + (size - 1) * 1j

    falling_bytes = parsed_data[:k]
    mapa = {}
    for x in range(size):
        for y in range(size):
            mapa[x + y * 1j] = 1 if x + y * 1j in falling_bytes else 0
    # print_matrix(mapa, size, size)
    # BFS
    queue = deque([start])
    visited = {}
    visited[start] = 0
    while queue:
        current = queue.popleft()
        cost = visited[current]
        for n in neighbors(current, mapa):
            if not n in visited:
                if n == goal:
                    return cost + 1
                visited[n] = cost + 1
                queue.append(n)

    return -1


def solve_part2(parsed_data: Any, size=71) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")

    for x in range(len(parsed_data), 0, -1):
        s = solve_part1(parsed_data, size, x)
        if s != -1:
            print(s, x, parsed_data[x])
            return (int(parsed_data[x].real), int(parsed_data[x].imag))

    return 0


# Uncomment and modify test data as needed
test_input = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_18.txt", "r") as f:
        input_data = f.read().strip()

    # Parse input
    parsed_data = parse_input(input_data)

    # Optional: Run tests
    if "test_input" in globals():
        print("🧪 Running tests...")
        test_parsed = parse_input(test_input)
        print(f"Test Part 1: {solve_part1(test_parsed, size=7, k =12)}")
        print(f"Test Part 2: {solve_part2(test_parsed, size=7)}")
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
