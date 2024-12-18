import time
import re
from typing import Any


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")

    register_pattern = r"Register (\w): (\d+)"
    program_pattern = r"Program: (.*)"
    registers = {}
    for r, v in re.findall(register_pattern, data):
        registers[r] = int(v)
    program = [int(x) for x in re.findall(program_pattern, data)[0].split(",")]

    # TODO: Modify parsing logic
    return (registers, program)


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    (registers, program) = parsed_data
    registers = registers.copy()
    print(registers, program)
    pointer = 0
    output = []
    while pointer < len(program):
        opcode = program[pointer]
        literal = program[pointer + 1]
        combo = [0, 1, 2, 3, registers["A"], registers["B"], registers["C"], None][
            literal
        ]
        print("pointer, opcode, literal, combo")
        print(registers, pointer, opcode, literal, combo)
        if opcode == 0:  # adv
            registers["A"] = registers["A"] // (2**combo)  # truncated
        elif opcode == 1:
            registers["B"] = registers["B"] ^ literal
        elif opcode == 2:
            registers["B"] = combo % 8
        elif opcode == 3:
            if registers["A"] > 0:
                pointer = literal
                continue
        elif opcode == 4:  # bxc
            registers["B"] = registers["B"] ^ registers["C"]
        elif opcode == 5:  # out
            output.append(combo % 8)
            print("output", combo % 8)
        elif opcode == 6:  # bdv
            registers["B"] = registers["A"] // (2**combo)  # truncated
        elif opcode == 7:  # cdv
            registers["C"] = registers["A"] // (2**combo)  # truncated
        pointer += 2
    print(registers)
    res = ",".join([str(x) for x in output])
    return res


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    (registers, program) = parsed_data
    registers = registers.copy()
    print(registers, program)
    goal = "".join([str(x) for x in program])
    for x in range(100):
        registers["A"] = x + parsed_data[0]["A"]
        registers["B"] = 0
        registers["C"] = 0
        pointer = 0
        output = []
        while pointer < len(program):
            opcode = program[pointer]
            literal = program[pointer + 1]
            combo = [0, 1, 2, 3, registers["A"], registers["B"], registers["C"], None][
                literal
            ]
            # print("pointer, opcode, literal, combo")
            # print(registers, pointer, opcode, literal, combo)
            if opcode == 0:  # adv
                registers["A"] = registers["A"] // (2**combo)  # truncated
            elif opcode == 1:
                registers["B"] = registers["B"] ^ literal
            elif opcode == 2:
                registers["B"] = combo % 8
            elif opcode == 3:
                if registers["A"] > 0:
                    pointer = literal
                    continue
            elif opcode == 4:  # bxc
                registers["B"] = registers["B"] ^ registers["C"]
            elif opcode == 5:  # out
                output.append(combo % 8)
                # print("output", combo % 8)
            elif opcode == 6:  # bdv
                registers["B"] = registers["A"] // (2**combo)  # truncated
            elif opcode == 7:  # cdv
                registers["C"] = registers["A"] // (2**combo)  # truncated
            pointer += 2
        print(registers)
        res = "".join([str(x) for x in output])
        print(goal, res == goal, res)
        if res == goal:
            print(x, res)
            return x

    return res


# Uncomment and modify test data as needed
test_input = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
test_input2 = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

test_input3 = """
Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0
"""
test_input2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
test_input3 = """
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
"""


if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_17.txt", "r") as f:
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

    """ # Solve part 1
    start_time = time.time()
    answer1 = solve_part1(parsed_data)
    time1 = time.time() - start_time
    print(f"✨ Part 1 answer: {answer1} (took {time1:.2f}s)\n")
    """

    # Solve part 2
    start_time = time.time()
    answer2 = solve_part2(parsed_data)
    time2 = time.time() - start_time
    print(f"✨ Part 2 answer: {answer2} (took {time2:.2f}s)")
