data = open("2024/8/data.in").read()
#data = open("2024/8/example.in").read()
grid = data.splitlines()

grid_values = set(data)
grid_values.remove(".")
grid_values.remove("\n")

rows = len(grid)
cols = len(grid[0])

all_positions = {k : [] for k in grid_values}
for row in range(rows):
    for col in range(cols):
        for value in grid_values:
            if grid[row][col] == value:
                all_positions[value].append((row, col))

antinodes = []
for key, positions in all_positions.items():
    for base_ix, base_position in enumerate(positions):
        for compare_ix, compare_position in enumerate(positions):
            if base_ix == compare_ix:
                continue
        
            row, col = base_position[0] - compare_position[0], base_position[1] - compare_position[1]

            antinode_row = base_position[0] + row
            antinode_col = base_position[1] + col
            
            check_rows = (antinode_row < rows) & (antinode_row >= 0)
            check_cols =  (antinode_col < cols) & (antinode_col >= 0)

            if check_rows & check_cols:
                antinodes.append((antinode_row, antinode_col))

pt1 = len(set(antinodes))
print("pt1:", pt1)

antinodes = []
for key, positions in all_positions.items():
    for base_ix, base_position in enumerate(positions):
        for compare_ix, compare_position in enumerate(positions):
            if base_ix == compare_ix:
                continue

            row, col = base_position[0] - compare_position[0], base_position[1] - compare_position[1]

            # number of diffs that fit in grid
            # this is a bit lazy as it really just needs to be distance from point to size, but cba to implement
            num_row_diffs = (rows - 1) // abs(row) 
            num_col_diffs = (cols - 1) // abs(col) 

            for i in range(min(num_row_diffs, num_col_diffs)):
                antinode_row = base_position[0] + (row * i)
                antinode_col = base_position[1] + (col * i)
                
                check_rows = (antinode_row < rows) & (antinode_row >= 0)
                check_cols =  (antinode_col < cols) & (antinode_col >= 0)

                if check_rows & check_cols:
                    antinodes.append((antinode_row, antinode_col))

pt2 = len(set(antinodes))

print("pt2:", pt2)