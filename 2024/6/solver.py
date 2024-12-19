grid = [[val for val in row] for row in open("2024/6/data.in").read().splitlines()] 
#grid = [[val for val in row] for row in open("2024/6/example.in").read().splitlines()]

rows, cols = len(grid), len(grid[0])

# define directions
lookup_direction = {
    "^" : (-1, 0),
    ">" : (0, 1),
    "<" : (0, -1),
    "v" : (1, 0)
}

lookup_move_key = {
    '^' : ">", 
    '>' : "v",
    '<' : "^",
    'v' : "<"
}

lookup_move_direction = {k : lookup_direction[v] for k, v in lookup_move_key.items()}

# recursive movement
def move_guard(grid, marks, row, col):
    key = grid[row][col] 
    if key in ['^', '>', '<', 'v']:
        marks.append((row, col))

        move_rows, move_cols = lookup_direction[key]
        
        new_row = row + move_rows
        new_col = col + move_cols
        
        if (new_row in [-1, rows]) or (new_col in [-1, cols]):
            return False, None

        if grid[new_row][new_col] == "#":
            move_rows, move_cols = lookup_move_direction[key]
            key = lookup_move_key[key]

            new_row = row + move_rows
            new_col = col + move_cols
        
        grid[row][col] = "."
        grid[new_row][new_col] = key

    return True, (grid, marks, new_row, new_col)

def get_start_position(grid):
    # find start location
    for row in range(rows):
        for col in range(cols):
            key = grid[row][col]
            if key in ['^', '>', '<', 'v']:
                start_row = row
                start_col = col

    return start_row, start_col

def print_grid(grid):
    print("\n")
    print("\n".join(["".join(row) for row in grid]))
    print("\n")

def copy_grid(grid):
    return [row[:] for row in grid]

def detect_repeating_pattern(positions, min_length = 5):
    n = len(positions)
    
    # Check all possible pattern lengths
    for pattern_length in range(min_length, n // 2 + 1):
        pattern = positions[:pattern_length]  # Candidate pattern

        # Check if the pattern repeats throughout the list
        for i in range(0, n, pattern_length):
            if positions[i:i + pattern_length] != pattern:
                repeating = False
                break

        # If the pattern repeats, return it
        if repeating:
            return pattern

    # No repeating pattern found
    return None

def is_repeating(positions, min_length = 5):
    n = len(positions)
    
    # Check all possible pattern lengths
    for pattern_length in range(min_length, n // 2 + 1):
        for i in range(len(positions)):
            pattern = positions[i:(i + pattern_length)]
            if pattern == positions[(i + pattern_length):(i + (pattern_length * 2))]:
                # double check
                if pattern == positions[(i + (pattern_length * 2)):(i + (pattern_length * 3))]:
                    return True
    return False

marks = []
moving_grid = copy_grid(grid) 
start_row, start_col = get_start_position(moving_grid)

present = True
args = (moving_grid, marks, start_row, start_col)
while present:
    present, args = move_guard(*args)

pt1 = len(set(marks))

print("pt1:", pt1)

max_count = 100000
repeat_check = 50

paradox_points = []

from tqdm import tqdm
loop = tqdm(total = len(marks))

for row in range(rows):
    for col in range(cols):
        # only run if guard came here in initial pass
        if (row, col) in marks:
            pass
        else:
            continue

        loop.update()

        moving = True

        moving_grid = copy_grid(grid)
        start_row, start_col = get_start_position(grid)

        # skip if blocker would go where guard starts
        if (row == start_row) & (col == start_col):
            continue

        moving_grid[row][col] = "#"
        args = (moving_grid, [], start_row, start_col)

        movements = []
        count = 0
        while moving:
            count += 1
            moving, args = move_guard(*args)
            
            if moving:
                movements.append((args[2], args[3]))
            #else:
                #print("natural exit")

            # check max iter
            if count > max_count:
                print("max count")
                paradox_points.append((row, col))
                moving = False

            # check repition
            if (count > 1000) & ((count % 200) == 0):
                if is_repeating(movements[-500:]):
                    print(movements[-500:])
                    paradox_points.append((row, col))
                    moving = False

            #if len(movements) > (repeat_check * 2):
                #if movements[-repeat_check:]  == movements[(-repeat_check*2):(-repeat_check)]:
                    #print("repeated")
                    #print(movements[-repeat_check:])
                    #print(movements[(-repeat_check*2):(-repeat_check)])
                    #paradox_points.append((row, col))
                    #moving = False

        #break
    #break
        #print_grid(moving_grid)

loop.close()
print(len(paradox_points))