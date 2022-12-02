def get_score(a, b):
    if a == 'A': # rock
        if b == 'X': # rock
            score = 1 + 3
        elif b == 'Y': # paper
            score = 2 + 6
        else: #scissors
            score = 3
    elif a == 'B': # paper
        if b == 'X': # rock
            score = 1
        elif b == 'Y': # paper
            score = 2 + 3
        else: #scissors
            score = 3 + 6
    else: #scissors
        if b == 'X': # rock
            score =  1 + 6

        elif b == 'Y': # paper
            score = 2

        else: #scissors
            score = 3 + 3
    return score

filename = "input/day02.txt"
# filename = "input/day02_sample.txt"

# part 1
with open(filename, 'r') as f:
    lines = f.readlines()
    total_score = 0
    for line in lines:
        a, b = line.split()
        score = get_score(a, b)
        total_score += score
print(total_score)

# part 2
with open(filename, 'r') as f:
    lines = f.readlines()
    total_score = 0
    for line in lines:
        a, result = line.split()
        
        b = ''
        if a == 'A': # rock
            if result == 'X': # lose
                b = 'Z'
            elif result == 'Y': # draw
                b = 'X'
            else: #win
                b = 'Y'
        elif a == 'B': # paper
            if result == 'X': # lose
                b = 'X'
            elif result == 'Y': # draw
                b = 'Y'
            else: # win
                b = 'Z'
        else: #scissors
            if result == 'X': # lose
                b = 'Y'
            elif result == 'Y': # draw
                b = 'Z'
            else: #win
                b = 'X'

        score = get_score(a, b)
        total_score += score
print(total_score)
