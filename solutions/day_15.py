import time
from typing import Any

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    labyrinth, instructions = data.strip().split("\n\n")

    mapa = {}
    orig = 0
    for y, row in enumerate(labyrinth.splitlines()):
        for x, e in enumerate(row):
            mapa[x + y * 1j] = e
            if e == "@":
                orig = y + x * 1j

    instructions = [[i for i in l] for l in instructions.splitlines()]
    return (mapa, instructions, orig)


def print_matrix(mapa):
    keys = mapa.keys()
    width = int(max([x.real for x in keys])) + 1
    height = int(max([x.imag for x in keys])) + 1
    print(width, height)
    res = ""
    for h in range(height):
        for w in range(width):
            res += mapa[w + h * 1j]
        res += "\n"
    print(res)
    return res


def move(i, pos, mapa):
    dic = {"<": -1, ">": 1, "^": -1j, "v": 1j}
    next_pos = dic[i] + pos
    # print(dic[i], pos, next_pos, mapa[next_pos])
    if not next_pos in mapa.keys():
        return (False, pos)
    if mapa[next_pos] == "#":
        return (False, pos)
    if mapa[next_pos] == ".":
        mapa[next_pos] = mapa[pos]
        mapa[pos] = "."
        return (True, next_pos)
    if mapa[next_pos] in ["O", "[", "]"]:
        can_move = move(i, next_pos, mapa)
        # print(can_move)
        if can_move[0]:
            mapa[next_pos] = mapa[pos]
            mapa[pos] = "."
            return (True, next_pos)
        else:
            return (False, pos)
    print("err:", mapa[next_pos], i, pos)


def move2(i, pos, mapa):
    dic = {"<": -1, ">": 1, "^": -1j, "v": 1j}
    if dic[i].imag == 0:
        return move(i, pos, mapa)
    next_pos = dic[i] + pos
    if not next_pos in mapa.keys():
        return (False, pos)
    if mapa[next_pos] == "#":
        return (False, pos)
    if mapa[next_pos] == ".":
        mapa[next_pos] = mapa[pos]
        mapa[pos] = "."
        return (True, next_pos)
    level = 0
    queue = [(0, set([pos]))]

    while True:
        next_level_queue = set()
        for n in queue[-1][1]:
            if mapa[n + dic[i]] == "#":
                return (False, pos)
            if mapa[n + dic[i]] == "[":
                next_level_queue.add(n + dic[i])
                next_level_queue.add(n + dic[i] + 1)
                continue
            if mapa[n + dic[i]] == "]":
                next_level_queue.add(n + dic[i])
                next_level_queue.add(n + dic[i] - 1)
                continue
        if next_level_queue:
            level += 1
            # print(queue, next_level_queue)
            queue.append((level, next_level_queue))
        else:
            break
    # print(queue)
    while queue:
        q = queue.pop()
        for x in q[1]:
            t = move(i, x, mapa)
        if q[0] == 0:
            return t
    return (False, pos)


def gps(mapa):
    keys = mapa.keys()
    width = int(max([x.real for x in keys])) + 1
    height = int(max([x.imag for x in keys])) + 1
    # print(width, height)
    res = 0
    for h in range(height):
        for w in range(width):
            if mapa[w + h * 1j] in ["O", "["]:
                res += int(h * 100 + w)
    return res


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    mapa, instructions, pos = parsed_data
    instructions = [i for l in instructions for i in l]
    mapa = mapa.copy()
    # print_matrix(mapa)

    for i in instructions:
        (_, pos) = move(i, pos, mapa)
        # print_matrix(mapa)
        # print(i)
        # wait = input("Press Enter to continue.")

    return gps(mapa)


def expand_mapa(mapa):
    keys = mapa.keys()
    width = int(max([x.real for x in keys])) + 1
    height = int(max([x.imag for x in keys])) + 1
    exp = {}
    for h in range(height):
        for w in range(width):
            if mapa[w + h * 1j] == "O":
                exp[(w * 2) + h * 1j] = "["
                exp[1 + (w * 2) + h * 1j] = "]"
            elif mapa[w + h * 1j] == ".":
                exp[(w * 2) + h * 1j] = "."
                exp[1 + (w * 2) + h * 1j] = "."
            elif mapa[w + h * 1j] == "#":
                exp[(w * 2) + h * 1j] = "#"
                exp[1 + (w * 2) + h * 1j] = "#"
            elif mapa[w + h * 1j] == "@":
                exp[(w * 2) + h * 1j] = "@"
                exp[1 + (w * 2) + h * 1j] = "."
                origin = (w * 2) + h * 1j
    return (exp, origin)


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    mapa, instructions, _ = parsed_data
    instructions = [i for l in instructions for i in l]
    # print_matrix(mapa)

    emapa, origin = expand_mapa(mapa)
    # print_matrix(emapa)
    for indx, i in enumerate(instructions):
        (_, origin) = move2(i, origin, emapa)
        if indx % 10 == 0:
            print_matrix(emapa)
            print(indx, i)
            clear_screen()
        # wait = input("Press enter")
    print_matrix(emapa)

    return gps(emapa)


# Uncomment and modify test data as needed
test_input = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_15.txt", "r") as f:
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
