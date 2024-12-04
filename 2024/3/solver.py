import re

data = open("2024/3/data.in").read().strip()
#data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# find locs of dos and donts
dos = [m.end() for m in re.finditer(r"do\(\)", data)]
donts = [m.end() for m in re.finditer(r"don\'t\(\)", data)]

# iterate over positions in data where you should do
do_ixs = []
do = True
for i in range(len(data)):
    if i in dos:
        do = True
    if i in donts:
        do = False
    
    if do:
        do_ixs.append(i)

pt1, pt2 = 0, 0

# iterate over matches
pattern = r'mul\(\d{1,3},\d{1,3}\)'
for m in re.finditer(pattern, data):
    group = m.group()

    # split into left and right matches
    # TODO: could also be regex
    comma_split = group.split(",")
    left = int(comma_split[0].split("(")[1])
    right = int(comma_split[1].split(")")[0])

    mul = (left * right)
    pt1 +=  mul
    
    # only add to pt2 if do active
    if m.start() in do_ixs:
        pt2 += mul
    
print("pt1:", pt1)
print("pt2:", pt2)