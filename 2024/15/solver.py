data = [[val for val in row] for row in open("2024/15/data.in").read().splitlines() if len(row) > 0]
#data = [[val for val in row] for row in open("2024/15/example1.in").read().splitlines() if len(row) > 0]
#data = [[val for val in row] for row in open("2024/15/example2.in").read().splitlines() if len(row) > 0]

def print_grid(grid):
    new = ["".join(row) for row in grid]
    print("\n".join(new)) 
    print("\n")

grid = []
directions = []
for row in data:
    if row[0] == "#":
        grid.append(row)
    else:
        directions += row

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        val = grid[row][col]
        if val == "@":
            pos = row, col  

movements = {
    "^" : (-1, 0),
    "<" : (0, -1),
    ">" : (0, 1),
    "v" : (1, 0)
}

for direction in directions:
    move = movements[direction]

    row, col = pos
    move_row, move_col = move
    new_row, new_col = row + move_row, col + move_col 
    
    new_val = grid[new_row][new_col]

    if new_val == "#":
        pos = row, col

    elif new_val == ".":
        grid[new_row][new_col] = "@"
        grid[row][col] = "."
        pos = new_row, new_col
        
    elif new_val == "O":
        move_positions = [(new_row, new_col)]

        # have this iterate differently depending on move  
        if direction == "^":
            iterator = range(row, -1, -1)
        elif direction == "<":
            iterator = range(col, -1, -1)
        elif direction == ">":
            iterator = range(col, cols)
        elif direction == "v":
            iterator = range(row, rows)

        for _  in iterator:
            move_row, move_col = move
            new_row, new_col = new_row + move_row, new_col + move_col 
            new_val = grid[new_row][new_col]

            if new_val == ".":
                # set end position to "O"
                grid[new_row][new_col] = "O"

                # change start position to "."
                change_row, change_col = move_positions[0]
                grid[change_row][change_col] = "@"
                pos = change_row, change_col

                # change original position to "."
                grid[row][col] = "."


                break
            elif new_val == "0":
                move_positions.append((new_row, new_col))
                continue
            elif new_val == "#":
                break
        
print_grid(grid)

pt1 = 0
for row in range(rows):
    for col in range(cols):
        val = grid[row][col]
        if val == "O":
            pt1 +=  (100 * row) + col

print("pt1:", pt1) 