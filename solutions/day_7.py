import time
from typing import Any


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.splitlines()
    eq = [
        (int(x), [int(e) for e in y.strip().split()])
        for l in lines
        for (x, y) in [l.split(":")]
    ]
    return eq


def generate_ternary_numbers(n, length):
    """Yields ternary numbers up to n-1, padded with trailing zeros to a specific length."""
    for i in range(n):
        ternary_num = ""
        num = i
        while num > 0:
            ternary_num = str(num % 3) + ternary_num
            num //= 3
        yield ternary_num.zfill(length)


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    count = 0
    for goal, nums in parsed_data:
        n = len(nums) - 1
        a = nums
        # print(goal, n, 2**n, nums)
        for i in range((2**n)):
            binary_str = bin(i)[2:].zfill(n)
            # print(binary_str)
            result = a[0] + a[1] if binary_str[0] == "0" else a[0] * a[1]
            for i in range(1, len(binary_str)):
                # print(goal, result, "+" if binary_str[i] == "0" else "x", a[i + 1])
                if binary_str[i] == "0":
                    result = result + a[i + 1]
                else:
                    result = result * a[i + 1]
                if goal < result:
                    # over
                    # print("over", goal, result)
                    break

            # print("res", result, binary_str)
            if goal == result:
                # print("GOAL")
                count += goal
                break
    return count


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    count = 0
    for goal, nums in parsed_data:
        n = len(nums) - 1
        a = nums
        for binary_str in generate_ternary_numbers(3**n, n):
            # print(binary_str)
            result = 0
            if binary_str[0] == "0":
                result = a[0] + a[1]
            elif binary_str[0] == "1":
                result = a[0] * a[1]
            else:
                result = int(f"{a[0]}{a[1]}")

            for i in range(1, len(binary_str)):
                if binary_str[i] == "0":
                    result = result + a[i + 1]
                elif binary_str[i] == "1":
                    result = result * a[i + 1]
                else:
                    result = int(f"{result}{a[i + 1]}")
                if goal < result:
                    break

            if goal == result:
                count += goal
                break
    return count


# Uncomment and modify test data as needed
test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_7.txt", "r") as f:
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
