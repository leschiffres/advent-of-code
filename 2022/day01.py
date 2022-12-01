filename = "input/day01.txt"
with open(filename, 'r') as f:
    lines = f.readlines()
    total_calories, max_calories = 0, 0
    for line in lines:
        if line.strip() == '':
            max_calories = max(max_calories, total_calories)
            total_calories = 0
        else:
            total_calories += int(line)

print(max_calories)

calories = []
with open(filename, 'r') as f:
    lines = f.readlines()
    total_calories = 0
    for line in lines:
        if line.strip() == '':
            calories.append(total_calories)
            total_calories = 0
        else:
            total_calories += int(line)

calories.sort(reverse=True)
print(sum(calories[0:3]))
