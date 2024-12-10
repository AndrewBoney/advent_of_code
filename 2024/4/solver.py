import re

"""
#data = open("2024/4/data.in").read().strip().splitlines()
data = "....XXMAS.\n.SAMXMS...\n...S..A...\n..A.A.MS.X\nXMASAMX.MM\nX.....XA.A\nS.S.S.S.SS\n.A.A.A.A.A\n..M.M.M.MM\n.X.X.XMASX"

data_all = "".join(data)

# forward
forward = re.findall("XMAS", data)
forward_count = len(forward)

# backward
backward = re.findall("XMAS", data[::-1])
backward_count = len(backward)

print(forward_count + backward_count)
"""

# pt1 (I gave up and used chatgpt)
def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    # Directions (row_delta, col_delta)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if word fits in this direction
                if all(
                    is_valid(r + i * dr, c + i * dc) and grid[r + i * dr][c + i * dc] == word[i]
                    for i in range(word_len)
                ):
                    count += 1

    return count

# Example word search
#"""
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]
#"""
#grid = open("2024/4/data.in").read().strip().splitlines()

# Convert grid to list of lists
grid = [list(row) for row in grid]

# Count occurrences of "XMAS"
result = count_xmas(grid)
print("Number of XMAS occurrences:", result)

# pt2

def count_mas(grid, word="MAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    # Directions (row_delta, col_delta)
    directions = [
        #(1, 1),   # Diagonal down-right
        #(-1, -1), # Diagonal up-left
        #(1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if word fits in this direction
                if all(
                    is_valid(r + i * dr, c + i * dc) and grid[r + i * dr][c + i * dc] == word[i]
                    for i in range(word_len)
                ):
                    count += 1

    return count

pt2 = count_mas(grid)

print("pt2:", pt2)