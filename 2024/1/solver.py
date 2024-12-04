from get_input import read_data

data = read_data("2024/1/data.in")

left, right = [], []
for row in data:
    l, r = row
    left.append(l), right.append(r)

# pt1
left_sorted, right_sorted = sorted(left), sorted(right)

diff = [abs(left_sorted[i] - right_sorted[i]) for i in range(len(data))]
pt1 = sum(diff)

print("p1:", pt1)

#pt2
right_counts = {}
for row in right:
    right_counts[row] = right_counts.get(row, 0) + 1

pt2 = 0

for row in left:
    pt2 += (row * right_counts.get(row, 0))

print("pt2:", pt2)