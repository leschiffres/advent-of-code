filename = "file1.txt"
with open(filename, 'r') as f:
    lines = f.readlines()
    print(lines)