import sys
f = open("in.txt")

line_count = int(f.readline())

for line_num in range(line_count):
    print line_num

    line = f.readline().split()
    combination_count = int(line.pop())

    combinations = {}
    
    for i in range(combination_count):
        combinations.add((line.pop(0), line.pop(0)), line.pop(0))

    print combinations

