import time
from typing import Any
from collections import defaultdict
from math import comb
from itertools import combinations
from tqdm import tqdm


def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = [l.split("-") for l in data.strip().splitlines()]

    return lines


def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    nodes = defaultdict(set)
    count = 0
    for a, b in parsed_data:
        nodes[a].add(b)
        nodes[b].add(a)

    combs = set()
    for k, v in tqdm(nodes.items()):
        if k.startswith("t"):
            for a, b in combinations(v, 2):
                if b in nodes[a]:
                    combs.add(frozenset(sorted([a, b, k])))
    # print(combs)
    # not 2429
    return len(combs)


def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    nodes = defaultdict(set)
    for a, b in parsed_data:
        nodes[a].add(b)
        nodes[b].add(a)

    best_clique = set()

    # For each node in sorted order
    for start_node in sorted(nodes.keys()):
        # Start with this node and its neighbors as potential clique
        potential_clique = {start_node} | nodes[start_node]

        while potential_clique:
            # Always check nodes in sorted order
            for node in sorted(potential_clique):
                # Check if this node connects to all others
                if not all(
                    other in nodes[node] for other in potential_clique if other != node
                ):
                    potential_clique.remove(node)
                    break
            else:
                # If we made it through without breaks, we found a clique
                if len(potential_clique) > len(best_clique):
                    best_clique = potential_clique.copy()
                break

    return ",".join(sorted(best_clique))


# Uncomment and modify test data as needed
test_input = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_23.txt", "r") as f:
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
