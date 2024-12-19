data = open("2024/7/data.in").read().splitlines()
#data = open("2024/7/example.in").read().splitlines()

correct = []
for line in data:
    split = line.split(":")

    assert len(split) == 2
    
    total = int(split[0])
    values = [int(i) for i in split[1].strip().split(" ")]

    left, right = [values[0]], values[1:]
    
    totals = left
    for i in range(len(right)):
        new_totals = []
        for out in totals:
            add_ = out + right[i]
            sum_ = out * right[i]

            new_totals.append(add_)
            new_totals.append(sum_)

        totals = new_totals            

    if total in totals:
        correct.append(total)

pt1 = sum(correct)

print("pt1:", pt1)