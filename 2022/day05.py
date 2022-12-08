# part 1

# filename = "input/day05_sample.txt"
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# ship = {
#     1: ['Z', 'N'],
#     2: ['M', 'C', 'D'],
#     3: ['P']
# }

filename = "input/day05.txt"

# [T]             [P]     [J]        
# [F]     [S]     [T]     [R]     [B]
# [V]     [M] [H] [S]     [F]     [R]
# [Z]     [P] [Q] [B]     [S] [W] [P]
# [C]     [Q] [R] [D] [Z] [N] [H] [Q]
# [W] [B] [T] [F] [L] [T] [M] [F] [T]
# [S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
# [Q] [Q] [B] [D] [J] [W] [H] [R] [J]
#  1   2   3   4   5   6   7   8   9 

ship = {
    1: ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
    2: ['Q', 'R', 'B'],
    3: ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
    4: ['D', 'V', 'F', 'R', 'Q', 'H'],
    5: ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
    6: ['W', 'R', 'T', 'Z'], 
    7: ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
    8: ['R', 'N', 'F', 'H', 'W'],
    9: ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']
}

with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        command = line.strip().split()
        num_boxes, crane_from , crane_to  = [int(command[i]) for i in range(len(command)) if i % 2 == 1]
        
        for _ in range(num_boxes):
            ship[crane_to].append(ship[crane_from].pop())

response = ''.join([ship[k][-1] for k in ship.keys()])
print(response)


# part 2

# filename = "input/day05_sample.txt"
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# ship = {
#     1: ['Z', 'N'],
#     2: ['M', 'C', 'D'],
#     3: ['P']
# }

filename = "input/day05.txt"

# [T]             [P]     [J]        
# [F]     [S]     [T]     [R]     [B]
# [V]     [M] [H] [S]     [F]     [R]
# [Z]     [P] [Q] [B]     [S] [W] [P]
# [C]     [Q] [R] [D] [Z] [N] [H] [Q]
# [W] [B] [T] [F] [L] [T] [M] [F] [T]
# [S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
# [Q] [Q] [B] [D] [J] [W] [H] [R] [J]
#  1   2   3   4   5   6   7   8   9 

ship = {
    1: ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
    2: ['Q', 'R', 'B'],
    3: ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
    4: ['D', 'V', 'F', 'R', 'Q', 'H'],
    5: ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
    6: ['W', 'R', 'T', 'Z'], 
    7: ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
    8: ['R', 'N', 'F', 'H', 'W'],
    9: ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']
}

# part 1
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        command = line.strip().split()
        num_boxes, crane_from , crane_to  = [int(command[i]) for i in range(len(command)) if i % 2 == 1]
        
        batch = []
        for _ in range(num_boxes):
            batch.append(ship[crane_from].pop())    
            
        batch = batch[::-1]
        ship[crane_to].extend(batch)

response = ''.join([ship[k][-1] for k in ship.keys()])
print(response)