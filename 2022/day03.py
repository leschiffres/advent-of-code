letters = 'abcdefghijklmnopqrstuvwxyz'
letters = letters + ''.join([l.upper() for l in letters])
print(letters)
priorities = {l:i+1 for i, l in enumerate(letters)}

filename = "input/day03.txt"
# filename = "input/day03_sample.txt"

# part 1
priorities_sum = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        
        mid = len(line) // 2
        left = set(line[:mid])
        right = set(line[mid:])
        for c in left.intersection(right):
            priorities_sum += priorities[c]

print(priorities_sum)

# part 2
priorities_sum = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    i  = 0
    while i < len(lines):
        common = set(lines[i].strip()).intersection(set(lines[i+1].strip())).intersection(set(lines[i+2].strip()))
        for c in common:
            priorities_sum += priorities[c]
        i = i + 3
        
print(priorities_sum)
