import time
from typing import Any
from collections import defaultdict, deque
import re

logical_ops = {
    "AND": lambda x, y: x and y,  # Boolean AND
    "OR": lambda x, y: x or y,  # Boolean OR
    "XOR": lambda x, y: int(bool(x) != bool(y)),  # Boolean XOR
}


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    r_initials = r"(\w+): (\d)"
    r_instructions = r"(\w+)\s(\w+)\s(\w+) -> (\w+)"

    init = re.findall(r_initials, data)
    instructions = re.findall(r_instructions, data)
    return (init, instructions)


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    (init, instructions) = parsed_data
    mapa = {}
    for k, v in init:
        mapa[k] = int(v)

    solve = deque(instructions)
    while solve:
        inst = solve.popleft()
        a, op, b, res = inst
        if a in mapa and b in mapa:
            mapa[res] = logical_ops[op](mapa[a], mapa[b])
        else:
            solve.append(inst)

    z_keys = sorted(
        [key for key in mapa.keys() if key.startswith("z")],
        key=lambda x: int(x[1:]),
        reverse=1,
    )

    z_values = [mapa[key] for key in z_keys]
    sol = "".join(str(x) for x in z_values)

    return int(sol, 2)


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    (init, instructions) = parsed_data
    return 0


# Uncomment and modify test data as needed
test_input = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_24.txt", "r") as f:
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
