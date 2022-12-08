from functools import cmp_to_key

def comparator(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] > y[1]:
            return -1
        elif x[1] < y[1]:
            return 1
        else:
            return 0
    return compare


filename = "input/day04.txt"

# part 1
overlapping_intervals = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        preprocessing = [[int(n) for n in assignment.split('-')] for assignment in line.strip().split(',')]
        intervals = sorted(preprocessing, key=cmp_to_key(comparator))
        if intervals[0][1] >= intervals[1][1]:
            overlapping_intervals += 1

print(overlapping_intervals)


# part 2
filename = "input/day04.txt"
overlapping_intervals = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        preprocessing = [[int(n) for n in assignment.split('-')] for assignment in line.strip().split(',')]
        intervals = sorted(preprocessing, key=cmp_to_key(comparator))
        if intervals[0][1] >= intervals[1][0]:
            overlapping_intervals += 1

print(overlapping_intervals)