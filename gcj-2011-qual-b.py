import sys
from collections import defaultdict

f = sys.stdin

line_count = int(f.readline())

for line_num in range(1, line_count + 1):
    line = f.readline().split()

    combination_count = int(line.pop(0))
    combinations = {}
    
    for i in range(combination_count):
        s = line.pop(0)
        combinations[(s[0], s[1])] = s[2]
        combinations[(s[1], s[0])] = s[2]

    opposition_count = int(line.pop(0))
    oppositions = defaultdict(list)

    for i in range(opposition_count):
        s = line.pop(0)
        oppositions[s[0]].append(s[1])
        oppositions[s[1]].append(s[0])

    element_count = line.pop(0)
    elements = line.pop()

    l = []
    for element in elements:
        l.append(element)
        
        if len(l) >= 2 and (l[-1], l[-2]) in combinations:
            l[-2:] = [combinations[(l[-1], l[-2])]]
        
        if l[-1] in oppositions:
            for item in oppositions[l[-1]]:
                if item in l:
                    l = []


    print "Case #" + str(line_num) + ": " + str(l).replace('\'', '')
