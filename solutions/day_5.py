import time
from typing import Any
from collections import defaultdict


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    (order, lines) = data.strip().split("\n\n")
    t = [o.split("|") for o in order.split("\n")]
    l = [l.split(",") for l in lines.split("\n")]
    return (t, l)


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    count = 0
    (rules, lines) = parsed_data
    rev = defaultdict(set)
    for a, b in rules:
        rev[a].add(b)

    for l in lines:
        line_set = set()
        for n in l:
            if rev[n].intersection(line_set):
                break
            line_set.add(n)
        else:
            #print(l)
            count += int(l[len(l) // 2])
            continue
    return count


def fix_order(line, rules):
    # while True:
    line_set = set()
    for i, n in enumerate(line):
        if rules[n].intersection(line_set):
            # we have to move n to before the min index and try with that
            j = min(line.index(e) for e in rules[n].intersection(line_set))
            del line[i]
            line.insert(j, n)
            #print("new", line)
        line_set.add(n)
    return line


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    count = 0
    (rules, lines) = parsed_data
    rev = defaultdict(set)
    for a, b in rules:
        rev[a].add(b)

    for l in lines:
        line_set = set()
        for n in l:
            if rev[n].intersection(line_set):
                new_l = fix_order(l, rev)
                count += int(new_l[len(l) // 2])

                break
            line_set.add(n)
        else:
            continue

    return count


# Uncomment and modify test data as needed
test_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_5.txt", "r") as f:
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
