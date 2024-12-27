data = open("2024/9/data.in").read().replace("\n", "")
#data = open("2024/9/example.in").read().replace("\n", "")

# first, convert to long block
id_ = 0
free = False
block = []
id_count = {}
for i, n in enumerate(data):
    n = int(n)

    if free: 
        block += ["."] * n # add n * "." to block
    else:
        id_count[id_] = n 
        block += [str(id_)] * n # add n * id_ to block
        id_ += 1 # iterate id

    free = not free # reverse free

og_block = block.copy()
reversed_block = block.copy()
reversed_block.reverse()

block_len = len(block)
num_dots = sum([1 if val == "." else 0 for val in block])
for ix, val in enumerate(reversed_block):
    dot_ix = block.index(".")
    if (block_len - dot_ix) == num_dots:
        break

    block[dot_ix] = val
    block[block_len - ix - 1] = "."

pt1 = 0
for ix, num in enumerate(block):
    if num == ".":
        break
    pt1 += int(num) * ix

print("pt1:", pt1)

## pt2
block = og_block.copy()

def count_dots_recursive(block, count):
    if len(block) <= 0:
        return count
    elif block[0] == ".":
        count += 1
        return count_dots_recursive(block[1:], count)
    else:
        return count

def count_dots(block):
    return count_dots_recursive(block, 0)

def get_dots(block):
    block_len = len(block)
    dot_lens = {}
    i = 0
    while True:
        if i >= block_len:
            break

        val = block[i]
        
        if val == ".":
            num_dots = count_dots(block[i:])
            dot_lens[i] = num_dots
            i += num_dots
        else:
            i += 1

    return dot_lens

block_len = len(block)

all_ids = sorted(list(id_count.keys()), reverse=True)
num_ids = len(all_ids)
first_id = {id_ : block.index(str(id_)) for id_ in all_ids}

dots = get_dots(block)
for id_ in all_ids:
    print(f"running {id_}")
    #dots = get_dots(block)
    #for dot_ix, len_ in dots.items():
    for dot_ix in sorted(dots):
        len_ = dots[dot_ix]
        num_ids = id_count[id_]
        if dot_ix > first_id[id_]:
            break
        if num_ids <= len_:
            for i in range(num_ids):
                block[dot_ix + i] = str(id_)
                block[first_id[id_] + i] = "."

            del dots[dot_ix]    
            
            new_dot_ix = dot_ix + num_ids
            new_dots = count_dots(block[(new_dot_ix):])
            if new_dots > 0:
                dots[new_dot_ix] = new_dots
                
            break

pt2 = 0
for ix, num in enumerate(block):
    if num == ".":
        continue
    pt2 += int(num) * ix

print("pt2:", pt2)