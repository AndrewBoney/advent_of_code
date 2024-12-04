from get_input import read_data

data = read_data("2024/2/data.in")

def is_safe(ls):
    """Determines if a report is safe, returning safety status and indices of unsafe levels."""
    inc_or_dec = (ls == sorted(ls)) or (ls == sorted(ls, reverse=True))

    if not inc_or_dec:
        return False
    else:
        for i in range(len(ls) - 1):
            diff = ls[i + 1] - ls[i]
            abs_diff = abs(diff)
            gap_ok = (1 <= abs_diff <= 3)

            if not gap_ok:
                return False
        return True

pt1, pt2 = 0, 0
for report in data:
    # Check if the report is safe initially
    safe = is_safe(report)

    safe_pt2 = safe
    if not safe_pt2:
        # iterate over removing each element and rerunning
        for ix in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(ix)

            safe_pt2 = is_safe(report_copy)
            if safe_pt2:
                break
    
    pt1 += int(safe)
    pt2 += int(safe_pt2)

print("pt1:", pt1)
print("pt2:", pt2)