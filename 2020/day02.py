filename = "input/day02.txt"

# part 1
total_valid = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        cardinality, letter, password = line.strip().split()
        lower, upper = [int(i) for i in cardinality.split('-')]
        letter = letter[0]
        
        total = 0
        for c in password:
            if c == letter:
                total += 1

        if lower <= total <= upper:
            total_valid += 1
print(total_valid)

# part 2
total_valid = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        cardinality, letter, password = line.strip().split()
        i, j = [int(i)-1 for i in cardinality.split('-')]
        letter = letter[0]
        
        if password[i] == letter and password[j] != letter:
            total_valid += 1
        
        if password[i] != letter and password[j] == letter:
            total_valid += 1
print(total_valid)