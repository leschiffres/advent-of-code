class Monkey():
    def __init__(self, items, operation, test_num, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.test_num = test_num
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspected_items = 0

    def inspect_next_item(self,):
        self.inspected_items += 1
        old = self.items.pop(0)
        new = eval(self.operation)

        # part 1
        # new = new // 3

        # part 2
        new = new % lcm
        if new % self.test_num == 0:
            return self.true_monkey, new 
        else:
            return self.false_monkey, new


    def receive_item(self, item):
        self.items.append(item)


filename = "input/day11.txt"
# filename = "input/day11_sample.txt"

monkeys = {}
total_monkeys = 0

with open(filename, 'r') as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        i = i + 1 # skip first line
        items = [int(item) for item in lines[i].split(':')[-1].strip().split(', ')]
        # print(items)
        i = i + 1
        operation = lines[i].split('=')[-1].strip()
        # print(operation)
        i = i + 1
        test_num = int(lines[i].strip().split()[-1])
        # print(test_num)
        i = i + 1  
        true_monkey = int(lines[i].strip().split()[-1])
        i = i + 1
        false_monkey = int(lines[i].strip().split()[-1])
        # print(true_monkey, false_monkey)
        i = i + 2
        monkeys[total_monkeys] = Monkey(items, operation, test_num, true_monkey, false_monkey)
        total_monkeys += 1

# for round in range(20): # part 1
# part 2
lcm = 1
for i in range(total_monkeys):
    lcm *= monkeys[i].test_num

for round in range(10000): # part 2
    if round != 0 and round % 1000 == 0:
        print(f"Round: {round}")
        for i in range(total_monkeys):
            print(f"\tMonkey {i} inspected {monkeys[i].inspected_items} items")
    for i in range(total_monkeys):
        while len(monkeys[i].items) > 0:
            next_monkey, item = monkeys[i].inspect_next_item()
            monkeys[next_monkey].receive_item(item)

inspections = sorted([monkeys[i].inspected_items for i in range(total_monkeys)])
print(inspections)
print(inspections[-1]* inspections[-2])