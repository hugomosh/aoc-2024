import time
from typing import Any
from tqdm import tqdm
from collections import defaultdict


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = [int(l) for l in data.strip().splitlines()]

    return lines


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    res = []
    for n in parsed_data:
        s = n
        for _ in range(2000):
            s = secret(s)
        res.append(s)
    return sum(res)


def mix(orig, num):
    return orig ^ num


def prune(num):
    return num % 16777216


def secret(num):
    res = num * 64
    res = mix(num, res)
    res = prune(res)
    res = mix(res // 32, res)
    res = prune(res)
    res = mix(res * 2048, res)
    res = prune(res)
    return res


def solve_part2_bruteforce0(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")

    pattern_sums = defaultdict(int)
    res = []
    for n in tqdm(parsed_data):
        s = n
        seq = [(n % 10, None)]
        for _ in range(1, 2000):
            prev = s % 10
            s = secret(s)
            seq.append((s % 10, s % 10 - prev))
        res.append(seq)

    possibles = set()
    sequences = []
    for r in tqdm(res, desc="Building sequences"):
        ss = []
        for i in range(3, len(r)):
            seq = (r[i - 3][1], r[i - 2][1], r[i - 1][1], r[i][1])
            possibles.add(seq)
            cost = r[i][0]
            ss.append((seq, cost))
        sequences.append(ss)
    # print("possibles")
    max_val = -1
    for p in tqdm(possibles, desc="Finding maximum"):
        bananas = 0
        for s in sequences:
            for i in range(len(s)):
                if s[i][0] == p:
                    bananas += s[i][1]
                    break
        if bananas > max_val:
            # print(p)
            max_val = bananas
    return max_val


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")

    pattern_sums = defaultdict(int)
    res = []
    for n in tqdm(parsed_data):
        s = n
        digits = []
        seen_patterns = set()

        prev_digit = s % 10
        digits.append((prev_digit,None))

        for _ in range(2000):
            s = secret(s)
            current_digit = s%10
            diff = current_digit - prev_digit
            digits.append((current_digit, diff))
            prev_digit = current_digit

            if len(digits)>= 4:
                pattern = tuple(digits[i][1] for i in range(-4,0))
                if pattern not in seen_patterns:
                    pattern_sums[pattern] += current_digit
                    seen_patterns.add(pattern)
    return max(pattern_sums.values())

# Uncomment and modify test data as needed
test_input3 = """
123
"""
test_input = """
1
2
3
2024
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_22.txt", "r") as f:
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
