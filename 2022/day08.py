# part 1

filename = "input/day08.txt"
# filename = "input/day08_sample.txt"

def print_grid(grid):
    for row in grid:
        print(row)
    print("*"*20)
with open(filename, 'r') as f:
    lines = f.readlines()
    grid = [[int(t) for t in line.strip()] for line in lines]

n, m = len(grid), len(grid[0])
visible = [[1 if i == 0 or i == n-1 or j ==0 or j == m-1 else 0 for j in range(m)]for i in range(n)]
# print_grid(grid)
# print_grid(visible)
# horizontally left to right

for i in range(1, n-1):
    max_tree = grid[i][0]
    for j in range(1, m):
        if grid[i][j] > max_tree:
            max_tree = grid[i][j]
            visible[i][j] = 1
# print("left to right")
# print_grid(visible)

# horizontally right to left
for i in range(1, n-1):
    max_tree = grid[i][m-1]
    for j in range(m-2, 0, -1):
        if grid[i][j] > max_tree:
            max_tree = grid[i][j]
            visible[i][j] = 1
# print("right to left")
# print_grid(visible)

# vertically top bottom

for j in range(1, m-1):
    max_tree = grid[0][j]
    for i in range(1, n-1):
        if grid[i][j] > max_tree:
            max_tree = grid[i][j]
            visible[i][j] = 1
# print("top bottom")
# print_grid(visible)    

# vertically bottom up

for j in range(m-1):
    max_tree = grid[n-1][j]
    for i in range(n-2, 0, -1):
        if grid[i][j] > max_tree:
            max_tree = grid[i][j]
            visible[i][j] = 1
# print("bottom up")
# print_grid(visible)

total = 0
for i in range(n):
    for j in range(m):
        if visible[i][j] == 1:
            total += 1
print(total)

# part 2

filename = "input/day08.txt"
# filename = "input/day08_sample.txt"
with open(filename, 'r') as f:
    lines = f.readlines()
    grid = [[int(t) for t in line.strip()] for line in lines]

# print_grid(grid)
n, m = len(grid), len(grid[0])

max_score = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        scenic_score = 1

        # search to left
        k = j-1
        left_score = 1
        while k >= 0 and grid[i][j] > grid[i][k]:
            if k > 0:
                left_score += 1
            k = k - 1

        # search to right
        k = j + 1
        right_score = 1
        while k < m and grid[i][j] > grid[i][k]:
            if k < m -1:
                right_score += 1
            k = k + 1

        # search to top
        k = i - 1
        top_score = 1
        while k >= 0 and grid[i][j] > grid[k][j]:
            if k > 0:
                top_score += 1
            k = k - 1

        # search to bottom
        k = i + 1
        bottom_score = 1
        while k < n and grid[i][j] > grid[k][j]:
            if k < n-1:
                bottom_score += 1
            k = k + 1

        scenic_score = left_score * right_score * top_score * bottom_score
        max_score = max(scenic_score, max_score)
        # print(f"({i}, {j}), {scenic_score}: ({left_score} * {right_score} * {top_score} * {bottom_score})")
print(max_score)