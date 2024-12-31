grid = [[i for i in row] for row in open("2024/12/data.in").read().splitlines()]
#grid = [[i for i in row] for row in open("2024/12/example.in").read().splitlines()]

rows = len(grid)
cols = len(grid[0])

all_values = set()
for row in range(rows):
    for col in range(cols):
        all_values.update(grid[row][col])

perimiters = {}
totals = {}

for k in all_values:
    perimiters[k] = []
    totals[k] = 0

movements = [
    (0, 0),
    (0, 1),
    (-1, 0),
    (-1, -1)
]

for row in range(rows):
    for col in range(cols):
        val = grid[row][col]
        for value in all_values:
            totals[value] += 1
            if val == value:
                for move_row, move_col in movements:
                    new_row, new_col = row + move_row, col + move_col
                    perimiters[val].append((new_row, new_col))
                    
print(all_values)