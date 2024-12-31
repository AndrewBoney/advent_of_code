import polars as pl

from tqdm import tqdm

data = [int(i) for i in open("2024/11/data.in").read().strip().split(" ")]
#data = [int(i) for i in open("2024/11/example.in").read().strip().split(" ")]

val_dict = {}

def apply_rules_fast(val):
    val_dict[val] = val_dict.get(val, apply_rules(val))
    return val_dict[val]

def apply_rules(val):
    if val == 0:
        return [1]
    else:
        str_val = str(val) 
        val_len = len(str_val) 
        if (val_len % 2) == 0:
            half = int(val_len / 2)
            return int(str_val[:half]), int(str_val[half:])
        else:
            return [val * 2024]

def apply_rules_pl(data):
    data = (data
        .with_columns(pl.col("nums").cast(pl.String).alias("strs"))
        .with_columns(pl.col("strs").n_chars().alias("str_len"))
        .with_columns(
            pl.when(pl.col("nums") == 0).then([1])
            .when((pl.col("str_len") % 2) == 0).then([pl.col("strs").str.slice(0, "str_len"), pl.col("strs").str.slice(0, "str_len")])
            .otherwise(pl.col("nums") * 2024)
            .alias("out")
        )
    )

    return data.explode("out")

def blink(data, blink_func=apply_rules):
    print(len(data))
    out = []
    for val in data:
        new = blink_func(val)
        for a in new:
            out.append(a)

    return out

def run_blinks(data, num_blinks, blink_func=apply_rules):
    for _ in tqdm(range(num_blinks)):
        data = blink(data)

    return data

def get_total_blinks(data, num_blinks, blink_func=apply_rules):
    return len(run_blinks(data, num_blinks))

pt1 = get_total_blinks(data, 25)

print("pt1:", pt1)

## pt2 defeats me...
## probably requires a loop that doesn't duplicate repeated values
pt2 = get_total_blinks(data, 75, apply_rules_fast)

print("pt2:", pt2)