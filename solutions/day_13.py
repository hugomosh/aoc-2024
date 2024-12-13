import re
import time
from typing import Any
import numpy as np


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    machine = data.split("\n\n")
    pattern = r"X[+=](\d+),\s*Y[+=](\d+)"
    res = [[(int(x), int(y)) for x, y in re.findall(pattern, m)] for m in machine]
    return res


def cost(eq1, eq2, total):
    """Solve
    Min 3A+B
    given A<= 100, B<=100
    axA + bxB = x
    ayA +byB = y
    """
    ax, ay = eq1
    bx, by = eq2
    x, y = total
    # print(f"{ax}A + {bx}B = {x}x, {ay}A + {by}B= {y}y")
    MAX_BUTTONS = 100
    best_sol = float("inf")
    best = None

    for A in range(MAX_BUTTONS):
        for B in range(MAX_BUTTONS):
            if (ax * A + bx * B) == x and (ay * A + by * B == y):
                print(A, B)
                if 3 * A + B < best_sol:
                    best_sol = 3 * A + B
                    best = (A, B)

    return (best_sol, best)


def is_effectively_integer(num):
    return abs(num - round(num)) < 1e-1


def solve(eq1, eq2, total):
    """Solve
    Min 3A+B
    given A<= 100, B<=100
    axA + bxB = x
    ayA +byB = y
    """
    ax, ay = eq1
    bx, by = eq2
    x, y = total
    print(f"{ax}A + {bx}B = {x}, {ay}A + {by}B = {y}")

    A = np.array([[ax, bx], [ay, by]])
    b = np.array([x, y])
    best_sol = float("inf")
    best = None

    try:
        solution = np.linalg.solve(A, b)
        a0, b0 = solution

        # Better handling of floating point precision
        if abs(a0 - round(a0)) < 10 and abs(b0 - round(b0)) < 10:
            a0, b0 = round(a0), round(b0)

            # Validate solution
            if a0 >= 0 and b0 >= 0:
                # Verify the solution actually satisfies the equations
                if (
                    abs(ax * a0 + bx * b0 - x) < 1
                    and abs(ay * a0 + by * b0 - y) < 1
                ):

                    obj_value = 3 * a0 + b0
                    if obj_value < best_sol:
                        best_sol = obj_value
                        best = (int(a0), int(b0))

    except np.linalg.LinAlgError:
        pass

    det = ax * by - ay * bx
    if det == 0:
        if ax * y != ay * x:  # Check if system is inconsistent
            print("System is inconsistent")
        else:
            # Handle dependent equations here if needed
            pass

    # Verify final solution
    if best is not None:
        a0, b0 = best
        print(f"Solution found: A={a0}, B={b0}")
        print(f"Verification:")
        print(f"Equation 1: {ax}*{a0} + {bx}*{b0} = {ax*a0 + bx*b0} (should be {x})")
        print(f"Equation 2: {ay}*{a0} + {by}*{b0} = {ay*a0 + by*b0} (should be {y})")
        print(f"Objective value (3A + B): {3*a0 + b0}")

    return (best_sol, best)


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    res = 0
    for eq in parsed_data:
        c = cost(*eq)
        # print(c)
        if c[0] != float("inf"):
            res += c[0]
    return res


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    res = 0
    for eq in parsed_data:
        x, y = eq[-1]
        c = solve(*eq[:2], (x + 10000000000000, y + 10000000000000))
        # print(c)
        if c[0] != float("inf"):
            res += c[0]
    return res


# Uncomment and modify test data as needed
test_input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_13.txt", "r") as f:
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
    # 40656741699544 not
    # 83197086729325 too low?
    # 85646091486525 not
    # 83197086729371
    # 85385414857248
    # 33607297722390
    # 36595185348437
    # 28721298423137
    # 30705407008351
    # 34030923897182
