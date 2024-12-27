#grid = [[int(i) for i in row] for row in open("2024/10/data.in").read().splitlines()]
grid = [[int(i) for i in row] for row in open("2024/10/example.in").read().splitlines()]

rows = len(grid)
cols = len(grid[0])

movements = [
    (0, 1), # right
    (0, -1), # left
    (-1, 0), # down
    (1, 0) # up
]

all_history = []

def make_move(grid, pos, move, history):
    row, col = pos
    move_row, move_col = move

    val = grid[row][col]
    if val == 9:
        all_history.append(history)
        return

    new_row = row + move_row
    new_col = col + move_col

    if (new_row >= 0) & (new_row < rows) & (new_col >= 0) & (new_col < cols):
        new_val = grid[new_row][new_col]
        if (new_val == (val + 1)):
            pos = (new_row, new_col)
            history.append(pos)
            for move in movements:
                make_move(grid, pos, move, history)            

for row in range(rows):
    for col in range(cols):
        val = grid[row][col]
        if val == 0:
            for move in movements:
                make_move(grid, (row, col), move, [])

for i in range(16):
    print(all_history[i])
    print("\n")

#print(all_history[:16])
#print(set(all_history))
print(len(all_history))