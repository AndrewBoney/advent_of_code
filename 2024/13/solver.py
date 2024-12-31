import re

from scipy.optimize import linprog

def parse_data(input_text):
    """
    Parses the claw machine configuration text into a structured list of dictionaries.

    Parameters:
    - input_text: A string containing the claw machine configurations.

    Returns:
    - A list of dictionaries, where each dictionary represents a claw machine.
    """
    machines = []
    # Regular expressions to extract the information
    button_a_pattern = r"Button A: X\+(\d+), Y\+(\d+)"
    button_b_pattern = r"Button B: X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"

    # Split input into sections for each machine
    machine_sections = input_text.strip().split("\n\n")

    for section in machine_sections:
        button_a_match = re.search(button_a_pattern, section)
        button_b_match = re.search(button_b_pattern, section)
        prize_match = re.search(prize_pattern, section)

        if button_a_match and button_b_match and prize_match:
            # Extract values
            button_a = (int(button_a_match.group(1)), int(button_a_match.group(2)), 3)  # Cost for A is always 3
            button_b = (int(button_b_match.group(1)), int(button_b_match.group(2)), 1)  # Cost for B is always 1
            prize = (int(prize_match.group(1)), int(prize_match.group(2)))

            # Add to machines list
            machines.append({
                "button_a": button_a,
                "button_b": button_b,
                "prize": prize
            })

    return machines

def solve_claw_machine(button_a, button_b, prize):
    """
    Solves the claw machine problem for a single machine.

    Parameters:
    - button_a: (x, y, cost) tuple for button A's movement and cost
    - button_b: (x, y, cost) tuple for button B's movement and cost
    - prize: (x, y) tuple for the prize location

    Returns:
    - A dictionary with the optimal number of presses for each button and the total cost.
    """
    # Coefficients of the objective function (costs for A and B presses)
    cost_a, cost_b = button_a[2], button_b[2]
    c = [cost_a, cost_b]

    # Coefficients for the constraints
    # x_A * button_a[0] + x_B * button_b[0] = prize[0] (X axis)
    # x_A * button_a[1] + x_B * button_b[1] = prize[1] (Y axis)
    A_eq = [
        [button_a[0], button_b[0]],  # X-axis constraint
        [button_a[1], button_b[1]]   # Y-axis constraint
    ]
    b_eq = [prize[0], prize[1]]  # Prize location

    # Bounds for the decision variables (non-negative integers)
    x_bounds = (0, None)  # Button A presses
    y_bounds = (0, None)  # Button B presses

    # Solve the linear programming problem
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[x_bounds, y_bounds], method='highs', integrality=1)

    if result.success:
        return {
            "button_a_presses": result.x[0],
            "button_b_presses": result.x[1],
            "total_cost": result.fun
        }
    else:
        return None
        #raise ValueError("No solution found for the given claw machine configuration.")

#data = open("2024/13/data.in").read()
data = open("2024/13/example.in").read()
machines = parse_data(data)

results = []
for i, machine in enumerate(machines):
    print(f"Machine {i}:")
    result = solve_claw_machine(machine["button_a"], machine["button_b"], machine["prize"])
    if result:
        print(f"  Button A presses: {result['button_a_presses']}")
        print(f"  Button B presses: {result['button_b_presses']}")
        print(f"  Total cost: {result['total_cost']} tokens")
        print()
    else:
        print(f"  No solution")

    results.append(result)

pt1 = sum([int(result["total_cost"]) for result in results if result])
print("pt1:", pt1)

machines_pt2 = []
for d in machines:
    out_d = d.copy()
    out_d["prize"] = (d["prize"][0] + 10000000000000, d["prize"][1] + 10000000000000)
    machines_pt2.append(out_d)

results_pt2 = []
for i, machine in enumerate(machines_pt2):
    print(f"Machine {i}:")
    result = solve_claw_machine(machine["button_a"], machine["button_b"], machine["prize"])
    if result:
        print(f"  Button A presses: {result['button_a_presses']}")
        print(f"  Button B presses: {result['button_b_presses']}")
        print(f"  Total cost: {result['total_cost']} tokens")
        print()
    else:
        print(f"  No solution")

    results_pt2.append(result)

pt2 = sum([int(result["total_cost"]) for result in results_pt2 if result])
print("pt2:", pt2)

# wrong answer pt2 :(