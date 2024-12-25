import time
from typing import Any
from collections import defaultdict, deque
import re
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

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
    G = nx.DiGraph()

    # Color mapping for operations
    op_colors = {
        "AND": "#FFA07A",  # Light salmon
        "OR": "#98FB98",  # Pale green
        "XOR": "#87CEFA",  # Light sky blue
    }

    # Add initial nodes with layer information
    for k, v in init:
        G.add_node(k, value=v, type="input", layer=0)

    # Process instructions
    solve = deque(instructions)
    for i, inst in enumerate(instructions):
        a, op, b, res = inst
        op_node = f"{op}_{i}"

        # Add nodes with layer information
        G.add_node(a, type="inter", layer=1)
        G.add_node(b, type="inter", layer=1)
        G.add_node(op_node, type="oper", op=op, layer=2)
        G.add_node(res, type="inter", layer=3)

        # Add edges
        G.add_edge(a, op_node)
        G.add_edge(b, op_node)
        G.add_edge(op_node, res)

    # Create layout using multipartite layout instead of spring_layout
    pos = nx.multipartite_layout(G, subset_key="layer")

    # Plot
    plt.figure(figsize=(20, 12))

    # Draw nodes by type
    # Input nodes
    input_nodes = [n for n, d in G.nodes(data=True) if d.get("type") == "input"]
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=input_nodes,
        node_color="lightgreen",
        node_shape="o",
        node_size=1000,
    )

    # Operation nodes with different colors based on operation type
    for op_type in ["AND", "OR", "XOR"]:
        op_nodes = [
            n for n, d in G.nodes(data=True) if d.get("type") == "oper" and op_type in n
        ]
        if op_nodes:
            nx.draw_networkx_nodes(
                G,
                pos,
                nodelist=op_nodes,
                node_color=op_colors[op_type],
                node_shape="s",
                node_size=800,
            )

    # Intermediate nodes
    inter_nodes = [n for n, d in G.nodes(data=True) if d.get("type") == "inter"]
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=inter_nodes,
        node_color="salmon",
        node_shape="o",
        node_size=1000,
    )

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True, arrowsize=20)

    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold")

    # Create legend
    legend_elements = [
        Patch(facecolor="lightgreen", label="Input Values"),
        Patch(facecolor=op_colors["AND"], label="AND Operation"),
        Patch(facecolor=op_colors["OR"], label="OR Operation"),
        Patch(facecolor=op_colors["XOR"], label="XOR Operation"),
        Patch(facecolor="salmon", label="Intermediate Values"),
    ]
    plt.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(1, 1))

    plt.title("Logic Circuit Graph")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

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
