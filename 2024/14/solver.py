def parse_data(file_path):
    p_list = []
    v_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by spaces and commas
            parts = line.strip().split()
            p_values = list(map(int, parts[0].split('=')[1].split(',')))
            v_values = list(map(int, parts[1].split('=')[1].split(',')))

            # Append to respective lists
            p_list.append(p_values)
            v_list.append(v_values)

    return p_list, v_list

def make_move(p, v):
    pr, pc = p
    vr, vc = v
    new_pr, new_pc  = pr + vr, pc + vc

    if new_pr < 0:
        new_pr = rows + new_pr

    if new_pr >= rows:
        new_pr = abs(new_pr - rows)

    if new_pc < 0:
        new_pc = cols + new_pc
    
    if new_pc >= cols:
        new_pc = abs(new_pc - cols)

    return new_pr, new_pc

def make_moves(ps, vs):
    return [make_move(p, v) for p, v in zip(ps, vs)]

def make_x_moves(ps, vs, num_moves):
    for _ in range(num_moves):
        ps = make_moves(ps, vs)
        print(ps)
    return ps

def count_totals(ps):
    mid_row, mid_col = (rows - 1) / 2, (cols - 1) / 2

    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for pr, pc in ps:
        if pr == mid_row or pc == mid_col:
            continue  # Skip robots in the middle row or column

        if pr < mid_row:
            if pc < mid_col:
                quadrants[0] += 1  # Top-left
            else:
                quadrants[1] += 1  # Top-right
        else:
            if pc < mid_col:
                quadrants[2] += 1  # Bottom-left
            else:
                quadrants[3] += 1  # Bottom-right

    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    return safety_factor

# Main logic
#file_path = '2024/14/example.in'
file_path = '2024/14/data.in'  
rows, cols = 101, 103
#rows, cols = 11, 7
num_moves = 100

ps, vs = parse_data(file_path)
ps = make_x_moves(ps, vs, num_moves)
safety_factor = count_totals(ps)

print("Safety Factor:", safety_factor)