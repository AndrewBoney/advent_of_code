#grid = [[int(i) for i in row] for row in open("2024/10/example.in").read().splitlines()]
grid = [[int(i) for i in row] for row in open("2024/10/data.in").read().splitlines()]

def make_move(grid, pos, move, history):
    row, col = pos
    move_row, move_col = move
    
    # Create a new history list for this path
    current_history = history.copy()
    current_history.append(pos)
    
    val = grid[row][col]
    if val == 9:
        return [current_history]  # Return list of successful paths
    
    paths = []
    new_row = row + move_row
    new_col = col + move_col
    
    if (new_row >= 0 and new_row < rows and 
        new_col >= 0 and new_col < cols):
        new_val = grid[new_row][new_col]
        if new_val == (val + 1):
            new_pos = (new_row, new_col)
            # Collect paths from all valid moves
            for next_move in movements:
                paths.extend(make_move(grid, new_pos, next_move, current_history))
    
    return paths

# Dictionary to store trailhead -> endpoints mapping
trailhead_paths = {}

rows = len(grid)
cols = len(grid[0])

movements = [
    (0, 1),   # right
    (0, -1),  # left
    (-1, 0),  # up
    (1, 0)    # down
]

# Find all trailheads and their paths
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 0:
            trailhead = (row, col)
            all_paths = []
            for move in movements:
                paths = make_move(grid, trailhead, move, [])
                all_paths.extend(paths)
            
            # Store unique endpoints for this trailhead
            endpoints = set()
            for path in all_paths:
                if path:  # If path exists
                    endpoints.add(path[-1])
            trailhead_paths[trailhead] = endpoints

# Calculate scores
total_score = 0
for trailhead, endpoints in trailhead_paths.items():
    score = len(endpoints)
    total_score += score
    print(f"Trailhead {trailhead} has score {score}")

print(f"Total score: {total_score}")