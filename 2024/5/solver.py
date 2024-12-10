import itertools

from tqdm import tqdm

data = open("2024/5/data.in").read().strip().splitlines()
#data = open("2024/5/example.txt").read().strip().splitlines()

rules = []
updates = []
for row in data:
    if "|" in row:
        rules.append([int(i) for i in row.split("|")])
    if "," in row:
        updates.append([int(i) for i in row.split(",")])

def is_valid_update(update, rules):
    for ix in range(len(update) - 1):
        left = update[ix]
        right = update[(ix + 1):]
        for ri in right:
            for rule in rules:
                right_rule, left_rule  = rule # rules flipped 
                if (left == left_rule) & (ri == right_rule):
                    return False  # Invalid update found
    return True

invalid_ix = [is_valid_update(update, rules) for update in updates]

valid_updates = []
invalid_updates = []
for i, b in enumerate(invalid_ix):
    if b:
        valid_updates.append(updates[i])
    else:
        invalid_updates.append(updates[i])

pt1 = sum([update[len(update) // 2] for update in valid_updates])

print("pt1:", pt1)

def flip_rules(update):
    update_len = len(update)
    for ix in range(update_len-1):
        left = update[ix]
        right = update[ix+1]
        for rule in rules:
            right_rule, left_rule  = rule # rules flipped 
            if (left == left_rule) & (right == right_rule):
                # overwrite update
                update = update[:(ix)] + [right] + [left] + update[(ix+2):]
                return flip_rules(update)
            
    return update

reordered_updates = []
for update in invalid_updates:
    update = flip_rules(update)
    reordered_updates.append(update)
    
pt2 = sum([update[len(update) // 2] for update in reordered_updates])

print("pt2:", pt2)

